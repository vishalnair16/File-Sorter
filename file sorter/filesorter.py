import os
import shutil

path = os.getcwd()+'/'

names = os.listdir(path)

folder_name = ['Images','Music']

for x in range(0,2):
     if not os.path.exists(path+folder_name[x]):
            os.makedirs(path+folder_name[x])
for files in names:
    if ".jpg" in files and not os.path.exists(path+'Image/'+files) or ".png" or "JPG":
           shutil.move(path+files , path+'Images/'+files)
    if ".mp3" in files and not os.path.exists(path+'Music/'+files):
        shutil.move(path+files , path+'Music/'+files)
