from urllib import request
import sys

myUrl = "http://adv400.tripod.com/kartinka.jpg"
myFile = "D:\\Python\\ADV_IT_python\\20_internet_huitinka.jpg"

try:
    print("Start downloading file from:" + myUrl)
    request.urlretrieve(myUrl, myFile)
except Exception:
    print("SI PEDER!!!")
    print(sys.exc_info())
    exit
print("File Downloaded successfully! Nisi peder, jebiga" + myFile)