#https://generatedata.com/generator - generate data
#https://regex101.com/ - check regexp

import re

input_filename = "19_in_datafile.txt"
output_filename = "19_out_result.txt"

inputfile = open(input_filename, mode = 'r', encoding='Latin-1')
outputfile = open(output_filename, mode = 'w', encoding='Latin-1')
mytext = inputfile.read()

#target = r"[\w.-]+@[A-Za-z-]+\.[\w.]+"
target = r"[\w.-]+@(?!yahoo\.edu)[A-Za-z-]+\.[\w.]+"

results = re.findall(target, mytext)

for item in results:
    print(item)
    outputfile.write(item + "\n")
print("\nTotal: " + str(len(results)))

#EXCLUDE 'intel.com' DOMAIN:
#target = r"[\w.-]+@?!intel\.com)[A-Za-z-]+\.[\w.]+"