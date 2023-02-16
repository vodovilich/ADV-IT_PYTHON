# Напишите здесь свой код :-)


router = {
            'model': 'cisco 4331',
            'ports_num': 4,
            'status': 'in use',
            'image': ['1.jpg', '2.jpg', '3.jpg']
}

print(router)


#to not create the same dictionary for every object, we create an array
all_routers = []


print(all_routers)

#DANGER - all entries are going to have the same data (change for one will aplly for all)
#for x in range(0, 10, 1):
#    all_routers.append(router)#
#CORRECT WAY - use .copy():

print("making 10 items\n")
for x in range(0, 10, 1):
    all_routers.append(router.copy())

print("Total number of devices: " + str(len(all_routers)))

for rtr in all_routers:
    print(rtr['model'])

print("\nChanging models: \n")

all_routers[3]['model'] = 'juniper MX240'
all_routers[7]['model'] = 'Mikrotik EBANOE GOVNO'

for rtr in all_routers:
    print(rtr['model'])

