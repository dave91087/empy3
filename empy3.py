import os, shutil
import mutagenx
from mutagenx.mp3 import MP3
from mutagenx.easyid3 import EasyID3
try:
    from mutagenx.easyid3 import EasyID3FileType
except ImportError:
    # Mutagen 1.17.
    from mutagenx.id3 import EasyID3FileType

indir = 'C:\\TEMP\\Music'
tempdir = 'C:\\TEMP\\NewMusic\\'
f = open("C:\\TEMP\\mp3s.txt", 'a')

for root, dirs, filenames in os.walk(indir):
    for fn in filenames:
        if os.path.isfile(os.path.join(root,fn)) and fn.endswith('.mp3'):
            test = mutagenx.File(os.path.join(root,fn), easy=True)
            print(fn+"\n")
            writestr = fn+"\t"+str(test["artist"])+"\t"+str(test["album"])+"\t"+str(test["tracknumber"])+"\t"+str(test["title"])+"\n"
            writestr = writestr.replace('[','').replace(']','')
            newpath =  tempdir+str(test["artist"])+"\\"+str(test["album"])+"\\"
            newname = str(test["title"])+".mp3"
            newpath = newpath.replace('[','').replace(']','').replace('\'','').replace('"','')
            newname = newname.replace('[','').replace(']','').replace('\'','').replace('"','').replace('/', '_').replace('?', '')
            f.write(writestr)
            f.write('"'+newpath+newname+'"\n')
            f.flush()
            writestr = ''
            if os.path.exists(newpath):
                shutil.copyfile(os.path.join(root,fn), newpath+newname)
            else:
                os.makedirs(newpath)
                shutil.copyfile(os.path.join(root,fn), newpath+newname)


        f.close
            #print(test.pprint())





#            print("Filepath "+os.path.join(root,fn))
#            print("Is MP3? "+str(fn.endswith('.mp3')))
#            print(fn);
            ##audio = MP3(os.path.join(root,fn), ID3=EasyID3)
            ##songtitle = audio["title"]
            ##artist = audio["performer"]
            ##album = audio["album"]
            ##genre = audio["genre"]
            ##encodedby = audio["author"]

            ##print(encodedby)
            #print(artist)
            #print(album)
            #print(audio.info.length, audio.info.bitrate)
            #audiofile = eyed3.load(os.path.join(root,fn))
            #print(file_obj)

