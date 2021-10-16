from random import randint
from time import sleep
listaJogos = []
todosJogos = []
cont = 0
print('-' * 50)
print('JOGOS DA MEGA SENA'.center(50))
print('-' * 50)
qtd = int(input('Quantos jogos vocêr quer que eu soreteie? '))
print('-=' * 5, f'SORTEANDO {qtd} JOGO(S)'.center(28), '-=' * 5)
for c in range(qtd):
    while cont < 6:
        num = randint(1, 60)
        if num in listaJogos:
            continue
        else:
            listaJogos.append(num)
            cont += 1
        if cont == 6:
            cont = 0
            break
    listaJogos.sort()
    todosJogos.append(listaJogos[:])
    listaJogos.clear()
for c in range(qtd):
    print(f'Jogo {c + 1}: {todosJogos[c]}')
    sleep(1)
print('-=' * 5, f'BOA SORTE'.center(28), '-=' * 5)