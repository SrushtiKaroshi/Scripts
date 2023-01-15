from sys import *

def function(value):
    print("Inside function with parameter : "+value)

def main():
    print("---- Function call in script -----")
    print("Application name : " +argv[0])

    if (len(argv) != 2):
        print("Error : Insufficient number of arguments")
        exit()
    
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("Function  ")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Use this script")
        exit()

    try:
        function(argv[1])

    except Exception as E:
        print("err"+E)

    if((len(argv)<1) or (len(argv)>3)):
       print("err")

if __name__ == "__main__":
    main()
