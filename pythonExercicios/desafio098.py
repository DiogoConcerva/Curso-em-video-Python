from time import sleep


def contador(inicio, fim, passo):
    if passo != 0:
        print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
        if passo > 0:
            if inicio < fim:
                for c in range(inicio, fim + 1, passo):
                    sleep(0.5)
                    print(c, end=' ')
                sleep(0.5)
                print('FIM!')
            else:
                for c in range(inicio, fim - 1, -passo):
                    sleep(0.5)
                    print(c, end=' ')
                sleep(0.5)
                print('FIM!')
        elif passo < 0:
            if inicio > fim:
                for c in range(inicio, fim - 1, -(abs(passo))):
                    sleep(0.5)
                    print(c, end=' ')
                sleep(0.5)
                print('FIM!')
            else:
                for c in range(inicio, fim - 1, abs(passo)):
                    sleep(0.5)
                    print(c, end=' ')
                sleep(0.5)
                print('FIM!')
    elif passo == 0:
        print(f'Contagem de {inicio} até {fim} de 1 em 1')
        if inicio > fim:
            for c in range(inicio, fim - 1, -1):
                sleep(0.5)
                print(c, end=' ')
            sleep(0.5)
            print('FIM!')
        else:
            for c in range(inicio, fim + 1, 1):
                sleep(0.5)
                print(c, end=' ')
            sleep(0.5)
            print('FIM!')


print('-=' * 30)
contador(1, 10, 1)
print('-=' * 30)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
print('-=' * 30)
