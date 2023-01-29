import psutil
import os
import time
from sys import *

def CreateFolder(FolderName = "demo"):
    Data = []
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        print("Folder is created")	
    else:
        print("Destination directory is already present")
        exit()
    return 

def main():
    print("---- Make folder in current directory -----")
    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Insufficient number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : It is used to create log file of running processes")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_Name Directory_Name")
        exit()

    CreateFolder(argv[1])

if __name__ == "__main__":
    main()
