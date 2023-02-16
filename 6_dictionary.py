# Напишите здесь свой код :-)

##############################
#
#
#       (-----item-----)
#       (-key-) (-value-)
#
#       keys should be UNIQUE
#
#
router = {
            'name': 'spb-gw',
            'location': 'spb',
            'status': 'free',
}

print(router)

print("Status = " + router['status'])

#ADDING a record
router['vendor'] = 'cisco'
print(router['vendor'])

#DELETING a record:
print("\nDELETING locatoin \n")
del router['location']
print(router)

#PRINTING ALL keys and values
print("\nDICTIONARY's content: \n")
print(router.keys())
print(router.values())
