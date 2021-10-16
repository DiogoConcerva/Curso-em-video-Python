from random import randint
from time import sleep
from operator import itemgetter

d = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
r = []
print('-' * 30)
print('Valores sortados:'.center(30))
print('-' * 30)
for k, v in d.items():
    sleep(1)
    print(f'{k} tirou {v}')
print('-' * 30)
r = sorted(d.items(), key=itemgetter(1), reverse=True)
print('Ranking dos jogadores:'.center(30))
print('-' * 30)
for c, v in enumerate(r):
    sleep(1)
    print(f"{c + 1}º lugar {v[0]} com {v[1]}")
