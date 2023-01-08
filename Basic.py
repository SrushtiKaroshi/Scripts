from sys import *

#def fun(Parameter):

def main():
    print("---- Basic template for script -----")
    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Insufficient number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("Name of script")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage of script")
        exit()

    #fun call

if __name__ == "__main__":
    main()
