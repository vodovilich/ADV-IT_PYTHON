import re

mytext = "ty pidor. A on net. On nije peder. Ty je.sam peder" \
        "hui wfoknqrjb ojan.fafjeongvuwe ojwrvuevu owrorewuvw Hyjtjnr" \
            "76574edrtfcgv 9-087yuhioqj 41f8yuhr 439hfy813yrq"

#print(mytext) - works ok

target = "\."
allresults = re.findall(target, mytext)

print(allresults) #LIKE GREP

"""
\d = Any digit is the first symbol
\D = Any symbol except digit
\w = Any alphabet symbol (A-Z a-z) (seems digits are also included)
\W = Any non-alphabet symbol
\s = breakspace
\S = non breakspace

[0-9]{3} == [0-9][0-9][0-9] == \d\d\d
[\w]{4}
[A-z][a-z]+
\. = . (period symbol) 
"""




