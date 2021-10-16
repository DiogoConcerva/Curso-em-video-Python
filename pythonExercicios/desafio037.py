n = int(input('Digite um número inteiro: '))
e = int(input('Escolha a base de conversão: 1 - Binário, 2 - Octal e 3 - Hexadecimal: '))

if (e == 1):
    binario = bin(n)
    print('O número {} em binário corresponde a {}'.format(n, binario))

elif (e == 2):
    octal = oct(n)
    print('O número {} em octal corresponde a {}'.format(n, octal))

elif (e == 3):
    hexa = hex(n)
    print('O número {} em hexadecimal corresponde a {}'.format(n, hexa))

else:
    print('\033[31m Você deve escolher 1, 2 ou 3!\033[m')
