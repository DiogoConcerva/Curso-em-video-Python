import random
from time import sleep

n = int(input('Tente adivinhar o número do computador: '))
nc = int(random.randrange(0, 6))

print('PROCESSANDO...')
sleep(3)
if (n == nc):
    print('Você acertou, ganhou o jogo, parabéns.')
else:
    print('Você errou, o número escolhido foi {}, tente novamente'.format(nc))
