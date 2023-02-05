import psutil
import os
import time
from sys import *

def CreateLogFile(FolderName = "demo"):
    Data = []
    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
    else:
        print("Destination directory is already present")
        exit()
    File_Path = os.path.join(FolderName,"one.log")
    fd = open(File_Path,"w")
    for proc in psutil.process_iter():
        value = proc.as_dict(attrs = ['pid','name','username'])
        Data.append(value)
    for element in Data:
        fd.write("%s\n"% element)

def main():
    print("---- Create log file in folder -----")
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
    CreateLogFile(argv[1])



if __name__ == "__main__":
    main()
