# Напишите здесь свой код :-)
def poslat_nahui(name):
    """
    Print "poshel nahui"
    """
    print("Poshel nahui!\nTy pidor, " + name)


def summa(x, y):
   s = x + y
   return s

poslat_nahui("Vasya")
poslat_nahui("Petya")
poslat_nahui("Huesos")

print("Vasya soset y Peti " + str(summa(5, 15)) + " chasov")




#FACTORIZATION FUNCTION
def factor(x):
    """Calculate factorial"""
    otvet = 1
    for i in range(1, x+1):
        otvet = otvet * i
    return otvet


print(factor(1))
print(factor(5))


for i in range(1, 10):
   print(str(i) + "!\t = " + str(factor(i)))

