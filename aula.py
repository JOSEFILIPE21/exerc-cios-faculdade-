import random
import time

lista = []

inicial = time.perf_counter()

for i in range(1,100000):
    numeros = random.randint(1,200000000000000)
    if numeros not in lista:
        lista.append(numeros)

#print(lista)
def bubbleSort( lista):
    contagem = 0
    n = len( lista)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j + 1]:
                ( lista[j], lista[j + 1]) = ( lista[j + 1], lista[j])
                contagem += 1

    #print(lista)
    
bubbleSort(lista)
final = time.perf_counter()
tempo = final - inicial
print(f"o primeiro codigo levou {tempo:.1f} segundos para ser executado")


inicial = time.perf_counter()
def indiceMenor(lista , inicio):
    minimo = inicio
    n = len( lista)
    for j in range( inicio + 1, n):
        if lista[ minimo] > lista[j]:
            minimo = j
    return minimo
indiceMenor(lista,0)

def selectionSort( lista):
    n = len( lista)
    for i in range(n - 1):
        minimo = indiceMenor(lista , i)
        ( lista[i], lista[ minimo]) = ( lista[ minimo], lista[i])
    
    #print(lista)
    #print(f"a segunda lista demorou {tempo} segundos")

selectionSort(lista)
final = time.perf_counter()
tempo = final - inicial
print(f"o segundo codigo levou {tempo:.1f} segundos para ser executado")