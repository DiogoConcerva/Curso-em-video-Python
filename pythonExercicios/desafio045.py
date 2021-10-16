import random

print('''Escolha:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura''')
e = int(input('Qual sua escolha: '))
c = random.randint(0, 2)

if (e == c):
    print('O jogo saiu empate, você escolheu {} e o computador também escolheu {}.'.format(e, c))

elif ((e == 0) and (c == 1) or (e == 1) and (c == 2) or (e == 2) and (c == 0)):
    print('O computador venceu, ele escolheu {} e você escolheu {}'.format(c, e))

elif ((e == 0) and (c == 2) or (e == 1) and (c == 0) or (e == 2) and (c == 1)):
    print('Você venceu, pois sua escolhe foi {} e a do computador foi {}'.format(e, c))

else:
    print('Sua escolha deve ser 0, 1 ou 2.')