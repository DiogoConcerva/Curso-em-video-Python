f = int(input('Digite o número que deseja calcular seu fatorial: '))
cont = f
fat = f
while cont != 1:
    cont -= 1
    f = f * cont
print('O fatorial de {}! é {}'.format(fat, f))
