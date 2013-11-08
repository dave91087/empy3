import os, shutil
import mutagenx
from mutagenx.mp3 import MP3
from mutagenx.easyid3 import EasyID3
try:
    from mutagenx.easyid3 import EasyID3FileType
except ImportError:
    # Mutagen 1.17.
    from mutagenx.id3 import EasyID3FileType

# Directories
fromDir = 'C:\\TEMP\\Music\\'
toDir = 'C:\\TEMP\\NewMusic\\'

# Logfile of sorts
f = open("C:\\TEMP\\mp3s.txt", 'a')

for root, dirs, filenames in os.walk(fromDir):
    for fn in filenames:
        if os.path.isfile(os.path.join(root,fn)) and fn.endswith('.mp3'):
            try:
                test = mutagenx.File(os.path.join(root,fn), easy=True)

                #Output to console to show progress
                print(fn+"\n")

                newpath =  toDir+str(test["artist"])+"\\"+str(test["album"])+"\\"
                newpath = newpath.replace('[','').replace(']','').replace('\'','').replace('"','')

                newname = str(test["title"])+".mp3"
                newname = newname.replace('[','').replace(']','').replace('\'','').replace('"','').replace('/', '_').replace('?', '')
                f.write('"'+newpath+newname+'"\n')
                f.flush()

                if os.path.exists(newpath):
                    shutil.copyfile(os.path.join(root,fn), newpath+newname)
                else:
                    os.makedirs(newpath)
                    shutil.copyfile(os.path.join(root,fn), newpath+newname)
            except:
                f.write('Error: '+fn+"\n")
                print('Error: '+fn)
                f.flush()
        f.close

# Unused Logging...
#writestr = fn+"\t"+str(test["artist"])+"\t"+str(test["album"])+"\t"+str(test["tracknumber"])+"\t"+str(test["title"])+"\n"
#writestr = writestr.replace('[','').replace(']','')
