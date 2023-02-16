# Напишите здесь свой код :-)
"""
name = input("Please enter your name: ")

print("poshel nahui, " + name)


age = input("Enter your age: ")
print("Your age is: " + age)
"""

"""
enter = ""
while enter != 'correct password':
    enter = input("Enter Password: ")

    print(enter + "  is a wrong password")
"""

"""
while True:
        enter = input("Enter Password: ")
        if enter == "correct password":
            break
        print(enter + " is a wrong password")
"""


mylist = []
msg = ""

while msg != 'stop':
    msg = input("enter new line and stop to finish: ")
    mylist.append(msg)

print(mylist)
