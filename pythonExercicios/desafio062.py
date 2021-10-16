t = int(input('Digite o termo: '))
r = int(input('Digite a razão: '))
print('=' * 50)
cont = 1
s = t
while cont <= 10:
    print('O {}º termo é {}'.format(cont, s))
    cont += 1
    s = s + r
print('=' * 110)
n = int(input('Você deseja imprimir mais algum termo? Se sim, quantos? Caso queira encerrar o programa digite 0: '))
cont = 1
print('=' * 110)
if (n == 0):
    print('O programa foi encerrado.')
    print('=' * 50)
else:
    while (cont <= n):
        print('O {}º termo é {}'.format(cont + 10, s))
        cont = cont + 1
        s = s + r
    print('=' * 50)