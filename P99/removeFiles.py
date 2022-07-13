import os
import shutil 
import time 

path = input("Enter file path: ")
days = time.time()
givenPath = os.path.exists(path)

if(givenPath == True):
    list_of_everything = os.walk(path)
    desiredTime = int(input("Enter the number of days you want your files to stay: "))
    
    ctime = int(os.stat(path).st_ctime)

    if(ctime > desiredTime):
        isFile = os.path.isfile(path)
        isDirectory = os.path.isdir(path)
        
        if(isFile):
            os.remove(path)
        if(isDirectory):
            shutil.rmtree(path)
    
        print("Files and Folder Deleted!")
else:
    print("Path does not exist")