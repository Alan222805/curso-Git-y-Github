from random import *

""" numeros = range(0, 21, 1)

lista = [n if n%2 == 0 else 'impar' for n in numeros]
    
print(lista) """


pies = [10,20,30,40]
metros = [round(p * 0.3048, 2) for p in pies]
print(metros)

print(sample(pies,2))

#Con comprension de listas, pasamos de eso 👇

""" lista_numeros = []
for numero in range(1, 10):
    aleatorio = randint(1, 50)
    if aleatorio % 2 == 0:
        lista_numeros.append(aleatorio) """
        
# A esto 👇
        
lista_numeros= [n for n in sample(range(1,50), 10) if n%2 == 0]

print(lista_numeros)