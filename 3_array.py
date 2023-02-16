# Напишите здесь свой код :-)
routers = ['spb', 'krak', 'snr', 'lviv', 'kyiv', 'dallas']
print(routers)
print(len(routers))
print(routers[0] + " " + routers[3])


#
#routers[6] = 'gdansk' - not allowed
#

#how to print the last one (number from the end)
print(routers[-1])

routers[1] = 'saratov'
print(routers)

routers.append('gdansk')
print(routers)

routers.insert(2, 'spb')
print(routers)

#del routers[2]
#print(routers)

#.remove removes ONLY the FIRST entry it finds
routers.remove('spb')
print(routers)

dead_router = routers.pop()
print("dead router is:" + dead_router)
print(dead_router)
print(routers)

#SORTING
routers.sort()
print(routers)
#routers.sort(reverse=True)

routers.reverse()
print(routers)
