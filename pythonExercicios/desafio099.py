from time import sleep


def maior(*numeros):
    if len(numeros) == 1 and numeros[0] == 0:
        print('Analisando os valores passados...')
        print(f'Foram informados 0 valores ao todo.')
        print(f'O maior valor informado foi 0')
    else:
        print('Analisando os valores passados...')
        for c in numeros:
            sleep(0.5)
            print(c, end=' ')
        print(f'Foram informados {len(numeros)} valores ao todo.')
        print(f'O maior valor informado foi {max(numeros)}')


print('-=' * 30)
maior(2, 9, 4, 5, 7, 1)
print('-=' * 30)
maior(4, 7, 0)
print('-=' * 30)
maior(1, 2)
print('-=' * 30)
maior(6)
print('-=' * 30)
maior(0)
print('-=' * 30)
