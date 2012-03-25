import sys
import commands

import features
import learn

def pred(fpath):

	songs = [fpath]
	d = features.report_features(songs, False)
	ex = d[fpath]
	s = "+1 "
	s = learn.extract_features(ex)
	f = open("test.data", 'w')
	f.write('+1 ' + s)
	f.close()
	
	print commands.getoutput("svm-predict test.data train.data.model pred.data")
	f = open('pred.data')
	mood = learn.find_key (learn.mood_map, int(f.readline()))
	
	print "{0} -> {1}".format (fpath, mood)
	return mood
	
if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "usgae learn.py <fpath>"
	else:
		pred(sys.argv[1])

