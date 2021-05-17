'''
Created on lunes, 3 de mayo de 2021
@author: Fabricio Cordova

https://github.com/Hiyperion

Descripcion:
    Notas del curso web scraping

    '''
# import random
# from random import randint
# from random import *

# ab=randint(3,4)


a,b=3,4 #definicion de bariables con ,


#* Casting: convertir una variable de un tipo a otro
x="1"
# x=int(x)
# x=x.
#_ en tipo de dato primitivo las asignaciones son por valor
x = 1
y= x
y= 2 #_ el valor de x se mantiene, es medio obvio, pero esto no sucede en estructuras más complejas, donde la asignacion es por referencia


a="hola"
z=a*5 #_repeticion
# print(z)

#* acronimos de operaciones sobre la misma variable
x = 3
x += 1
x -= 1
x *= 2


#* FOrmas de importar libreria

# import random
# from random import randint
# from random import *
# import random as rd


# x=input("ingrese: ")

x=str("48")
x=float("54.5")
x=float("59")
print(x)

#* elif es una segunda condicion
a = 5
if a>5:
    print("a")
elif a<5:
    print(a-12)
else:
    print("hola")

import random

x=random.randint(1,5)
if x==1:
    print("soy el numero uno")
elif x==2:
    print("Hola soy el numero dos")
else:
    print("no soy ")

# for i in range(10):
#     x += random.randint(1,5)
# print(x)

# while x != 5:
#     x=random.randint(1,100)
#     print(x)

listA=[1,2,3,4,2]
listA.remove(2)#borra la primera coincidencia
print(listA)
print(3 in listA)
listA.reverse()
print(listA)


#* split y join

A="Banana,Col,Fresa"

L=A.split(",")
print(L)
L2="_".join(L)
print(L2)




res1=True
res2=False
res3=True
print(res1+res2)
a=[1,2,3]
b=a
b[1]=50
print(a)

a=a+b
print(a[-3:-1])

a=["a","b","c"]

print("".join(a))

#* CONJUNTOS a={5,2,9} NO tienen indice, no almacenan repetidos, se puede intersecar, unir 
