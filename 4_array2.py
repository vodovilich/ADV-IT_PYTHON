# Напишите здесь свой код :-)
routers = ['spb', 'krak', 'lviv', 'kharkiv']

print(routers)

for router in routers:
    print(router.upper())

for x in range(1, 10, 1):
    print(x)

num_list = list(range(0, 10))
print(num_list)

for x in num_list:
    x = x * 2
    print(x)

num_list.reverse()
print(num_list)

print("MAX number is: " + str(max(num_list)))
print("MIN number is: " + str(min(num_list)))
print("SUM value is: " + str(sum(num_list)))

#routers[0:2] - entries 0 and 1, equals to array[:2]
rtrs_free = routers[0:2]
print(rtrs_free)
rtrs_free = routers


#HOW TO COPY AN ARRAY
##HUEVO:
print("ROUTERS: " + str(routers))
print("RTS_FREE: " + str(rtrs_free))
print("removing routers[-1]")
del routers[-1]
print("ROUTERS: " + str(routers))
print("RTS_FREE: " + str(rtrs_free))
print("PIZDOS - last entry in rtrs_free was also removed - OMG\n\n")


##GOOD:
rtrs_free = routers[:]
print("ROUTERS: " + str(routers))
print("RTS_FREE: " + str(rtrs_free))
print("removing routers[-1]")
del routers[-1]
print("ROUTERS: " + str(routers))
print("RTS_FREE: " + str(rtrs_free))
