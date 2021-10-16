import random

p = input('Digite o primeiro nome: ')
s = input('Digite o segundo nome: ')
t = input('Digite o terceiro nome: ')
q = input('Digite o quarto nome: ')

print('Quem vai apagr o quadro é {}'.format(random.choice([p, s, t, q])))
