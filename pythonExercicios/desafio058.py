import random
c = int(random.randint(0, 10))
u = int(input('Ja pensei no meu número, tenta adivinhar entre 0 e 10: '))
t = 1
while (c != u):
    u = int(input('Você errou, tente novamente: '))
    t = t + 1
print('Parabéns, você acertou o número que pensei, {}, na {}ª tentativa'.format(c, t))
