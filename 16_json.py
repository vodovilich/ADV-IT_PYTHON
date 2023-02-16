import json
filename = "16_json_devices.txt"
myfile = open(filename, mode='w')

device1 = {
    'FQDN': "iol-157-rtr-01",
    'SerNum': "PEDER123",
    'Model': "Cisco 1488",
    'Licenses': ['ipbase', 'securityk9', 'hseck'],
    'Ports': 4,
}

device2 = {
    'FQDN': "iol-157-rtr-02",
    'SerNum': "PEDER125",
    'Model': "Cisco 1469",
    'Licenses': ['ipbase', 'securityk9'],
    'Ports': 5,
}

mydevices = []
mydevices.append(device1)
mydevices.append(device2)
#======================SAVE BY JSON=================================
json.dump(mydevices, myfile)
myfile.close()
print("ty pidor")

#======================OPEN BY JSON=================================

myfile = open(filename, mode='r')
json_data = json.load(myfile)

for dev in json_data:
    print("FQDN is " + dev['FQDN'])
    print("AVAILABLE PORTS =" + str(dev['Ports']))
    print("LICENSES INSTALLED: " + dev['Licenses'][0])
    print("LICENSES INSTALLED: " + dev['Licenses'][1])
#    print("LICENSES INSTALLED: " + dev['Licenses'][2]) - leads to IndexError: list index out of range
    for num, lic in enumerate(dev['Licenses'], 1):
        print(dev['FQDN'] + " license #" + str(num) + " = " + lic)
    print("\n\n")