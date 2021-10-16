n = int(input('Digite um número para saber se ele é primo ou não: '))
cont = 0
for c in range(1, n + 1):
    if ((n % c) == 0):
        cont = cont + 1
if(cont == 2):
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não é primo.'.format(n))
