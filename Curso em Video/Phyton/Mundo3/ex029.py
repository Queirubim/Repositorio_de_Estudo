from random import randint
from time import sleep
num = list()
s = 0


def sort(numerps):
    num.clear()
    for c in range(0, 5):
        num.append(randint(1, 10))


def somapar(lista):
    global s
    for c in lista:
        if c % 2 == 0:
            s += c
    return s


sort(num)
somapar(num)
print(f'Sorteando 5 valores da lista: ', end='')
for numero in num:
    print(numero, end=' ')
    sleep(0.3)
print('Pronto')
print(f'Somando os valores pares de {num}, temos {s}.')
