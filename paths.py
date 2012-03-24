import os
files_list = []
music_directory = "/var/lib/mpd/music"

def get_file_list():
    global files_list
    files_list = []
    listFiles(music_directory)
    return files_list

def listFiles(dir):
    basedir = dir
    subdirlist = []         # 
    for item in os.listdir(dir):
        if os.path.isfile(os.path.join(dir,item)):
            files_list.append(os.path.join(dir,item))
        else:
            subdirlist.append(os.path.join(basedir, item))

    for subdir in subdirlist:
        listFiles(subdir)

