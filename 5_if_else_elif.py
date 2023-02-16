# Напишите здесь свой код :-)

#

"""
age = 323

if age <= 31:
    print("ty pizdyuk")
elif (age > 31) and (age < 40):
    print("ty pidor")
else:
    print("ty stari hui")

"""

all_routers = ['spb', 'krak', 'snr', 'dallas']
us_rtrs= ['snr', 'dallas']

if 'snr' in us_rtrs:
    print('snr is american')
else:
    print("snr is not american")



for xxx in all_routers:
    if xxx in us_rtrs:
        print(xxx + " is American")
    else:
        print(xxx + " is not American")
