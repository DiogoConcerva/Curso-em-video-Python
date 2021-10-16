from random import randint
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
n = int(input('Digite um valor: '))
e = str(input('Par ou Ímpar [P / I]: ')).strip().upper()
print('-' * 40)
c = randint(0, 10)
v = n + c
venceu = 0
while (v % 2 == 0) and (e == 'P'):
    print(f'Você jogou {n} e o computador {c}. Total de',n + c,'deu PAR.')
    print('Você VENCEU!')
    print('Vamos jogar novamente...')
    venceu = venceu + 1
    print('=-' * 20)
    n = int(input('Digite um valor: '))
    e = str(input('Par ou Ímpar [P / I]: ')).strip().upper()
    print('-' * 40)
    c = randint(0, 10)
    v = n + c
    while (v % 2 == 1) and (e == 'I'):
        print(f'Você jogou {n} e o computador {c}. Total de', n + c, 'deu ÍMPAR.')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        venceu = venceu + 1
        print('=-' * 20)
        n = int(input('Digite um valor: '))
        e = str(input('Par ou Ímpar [P / I]: ')).strip().upper()
        print('-' * 40)
        c = randint(0, 10)
        v = n + c
print(f'GAMER OVER! Você venceu {venceu} vezes.')
