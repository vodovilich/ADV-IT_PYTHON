
import sys

filename = 'does_not_exist.txt'
#filename = 'file2.txt'


while True:
    try:
        print("\nINSIDE OF TRY\n")
        myfile = open(filename, mode='r', encoding='latin_1')

    #except Exception - means ANY ERROR
    except Exception:
        print("\nINSIDE OF EXCEPT")
        print("ERROR FOUND! TY PIDOR!\n")
        #sys.exit() - to exit the programm, but requires sys module to be imported
        #sys.exc_info()[1] - means that show only the [1] element of array
        print(sys.exc_info()[1])
        filename = input("Enter correct file name: ")
    else:
        print("\nINSIDE OF ELSE")
        print(myfile.read())
        sys.exit()

#finally - optional, not required. Just "continue executing" - but seems not exactly...
#finally executed even after sys.exit() in else.

    finally:
        print("INSIDE OF FINALLY")
print("===========EOF=========")