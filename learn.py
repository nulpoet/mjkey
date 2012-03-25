import sys
import json

feature_map = {}

feature_map['energy'] = 1
feature_map['loundess'] = 2
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
feature_map['danceability'] = 18

mood_map = {}
mood_map['energetic'] = 0
mood_map['positive'] = 1
mood_map['dark'] = 2
mood_map['calm'] = 3

def find_key(dic, val):
    """return the key of dictionary dic given the value"""
    return [k for k, v in dic.iteritems() if v == val][0]

def extract_features(ex):
	s = ""
	for fid in range(1, 19):
		s += " {0}:{1}".format (fid, ex['features'][ find_key(feature_map, fid) ])
	return s

def learn(fpath, outfpath):
	outf = open(outfpath, 'w')
	examples = open(fpath).read().split('\n\n')
	
	for exj in examples[:-1]:
		ex = json.loads(exj)
		
		print ex, '------'
		
		s = "+" + str(mood_map[ex['category']])
		s = extract_features(ex)
		s += '\n'		
		outf.write(s)
		
if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "usgae learn.py <alldump.txt> <otput file>"
	else:
		learn(sys.argv[1], sys.argv[2])
