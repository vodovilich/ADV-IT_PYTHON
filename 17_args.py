import sys
import os
print("\nty pidor\n")


#arguments go into a programm as an array sys.argv

print(sys.argv[0:])

x = len(sys.argv)

if x > 1:
    if sys.argv[1] == "-h":
        print("Help requested")
        print("USE: python.exe args.py argv1 argv2")
    print("Argument entered: " + str(sys.argv[1:]))
else:
    print("No arguments provided")

os.system("dir > 17_test.txt")
#os.mkdir("17_createdDir")
sys.exit()
#sys.exit(2) - EXITS WITH ERROR CODE 2

