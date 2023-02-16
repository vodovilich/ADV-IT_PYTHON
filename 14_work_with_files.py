import os

inputfile = "14_in_file.txt"
#utf-8 and latin_1 encoding are zaebis
#

myfile = open(inputfile, mode='r', encoding = 'ascii')
#print(myfile.read())


outputfile = "14_out_file2.txt"
myfile2 = open(outputfile, mode = 'w', encoding='latin_1')


#method .strip() - removes empty strings
#for line in myfile:
#    print("Bad pas is " + line.strip())

"""
line - every string from file
num - string number
"""
for num, line in enumerate(myfile, 1):
    if line.strip():
        print("Line " + str(num) + ": " + line.strip())
        myfile2.write(line)

# if "word" in line - works as grep
# myfile2.write WORKS AS >, not ">>" - all previous content is removed nahui
#to add - use file = open(mode = 'a')


# if line.strip(): - means that line IS NOT EMPTY

myfile.close()
myfile2.close()