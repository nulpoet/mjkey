#!/usr/bin/python
import commands
import json
import urllib2
import pickle
import time

def report_features(songlist):
	song_map= {};
	song_feature = {};
	feature_map = {};
	mood_map = {};
	
	feature_map['danceability'] = 0
	feature_map['energy'] = 1
	feature_map['loudness'] = 2
	feature_map['speechiness'] = 3
	feature_map['tempo'] = 4
	feature_map['timbre0'] = 5
	feature_map['timbre1'] = 6
	feature_map['timbre2'] = 7
	feature_map['timbre3'] = 8
	feature_map['timbre4'] = 9
	feature_map['timbre5'] = 10
	feature_map['timbre6'] = 11
	feature_map['timbre7'] = 12
	feature_map['timbre8'] = 13
	feature_map['timbre9'] = 14
	feature_map['timbre10'] = 15
	feature_map['timbre11'] = 16
	feature_map['time_sign'] = 17 

	print "Started at ", time.asctime()
	
	for song in songlist:
		#print song;
		#if(song[len(song)-4 : len(song)-1] != 'mp3'):
		#	continue
		
		f = open("/home/rohit/Desktop/dump.txt", "a");

		s = "curl -X POST -H \"Content-Type:application/octet-stream\" \"http://developer.echonest.com/api/v4/track/upload?api_key=OXT5F9WRYSKSVOK71&filetype=mp3\" --data-binary \"@" + song + "\"";
	
		upload_output = commands.getoutput(s);
		temp = json.loads(upload_output[upload_output.find("{"):upload_output.__len__()]);
		#output_split = upload_output.split("\"");
		md5 = temp['response']['track']['md5']
		
		
		s = "curl -F \"api_key=OXT5F9WRYSKSVOK71\" -F \"format=json\" -F \"md5="+md5+"\" -F \"bucket=audio_summary\" \"http://developer.echonest.com/api/v4/track/analyze\""

		analyse_output = commands.getoutput(s);
		dict_feat = json.loads(analyse_output[analyse_output.find("{"):analyse_output.__len__()]);
		
		url = dict_feat['response']['track']['audio_summary']['analysis_url'];
		
		data = urllib2.urlopen(url).read();
		js = json.loads(data)
		
		timbre_vec = [0,0,0,0,0,0,0,0,0,0,0,0]

		for t in js['segments']:
			for i in range(12):
				timbre_vec[i] += t['timbre'][i]
				
		for i in range(12):
			timbre_vec[i] /= len(js['segments'])
		
		song_feature[song] = {}
		song_feature[song]['features']={}
		song_feature[song]['features']['danceability'] = dict_feat['response']['track']['audio_summary']['danceability']
		song_feature[song]['features']['energy'] = dict_feat['response']['track']['audio_summary']['energy']
		song_feature[song]['features']['loundess'] = dict_feat['response']['track']['audio_summary']['loudness']
		song_feature[song]['features']['speechiness'] = dict_feat['response']['track']['audio_summary']['speechiness']
		song_feature[song]['features']['tempo'] = dict_feat['response']['track']['audio_summary']['tempo']
		song_feature[song]['features']['timbre0'] = timbre_vec[0]
		song_feature[song]['features']['timbre1'] = timbre_vec[1]
		song_feature[song]['features']['timbre2'] = timbre_vec[2]
		song_feature[song]['features']['timbre3'] = timbre_vec[3]
		song_feature[song]['features']['timbre4'] = timbre_vec[4]
		song_feature[song]['features']['timbre5'] = timbre_vec[5]
		song_feature[song]['features']['timbre6'] = timbre_vec[6]
		song_feature[song]['features']['timbre7'] = timbre_vec[7]
		song_feature[song]['features']['timbre8'] = timbre_vec[8]
		song_feature[song]['features']['timbre9'] = timbre_vec[9]
		song_feature[song]['features']['timbre10'] = timbre_vec[10]
		song_feature[song]['features']['timbre11'] = timbre_vec[11]
		song_feature[song]['features']['time_sign'] = dict_feat['response']['track']['audio_summary']['time_signature']
		
		
		f.write(song+"\n"+pickle.dumps(song_feature[song])+"\n\n")

		f.close()
		
		print time.asctime(), song, "done"
		
	#print song_feature;
	return song_feature;
	
#list_song = ["/home/rohit/Music/Rockstar (2011)/10 - Rockstar - Saadda Haq !Ezio!.mp3"]
#print report_features(list_song);

