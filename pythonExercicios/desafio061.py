t = int(input('Digite o termo: '))
r = int(input('Digite a razão: '))
cont = 1
s = t
while cont <= 10:
    print('O {}º termo é {}'.format(cont, s))
    cont += 1
    s = s + r
