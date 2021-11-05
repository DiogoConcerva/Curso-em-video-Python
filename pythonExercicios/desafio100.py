from random import randint
from time import sleep


def somarPar(numneros):
    soma = 0
    for c in numneros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {numneros}, temos {soma}')


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    numeros = []
    for c in range(0, 5):
        sleep(0.5)
        numeros.append(randint(1, 10))
        print(numeros[c], end=' ')
    print('PRONTO!')
    somarPar(numeros)


sorteia()
