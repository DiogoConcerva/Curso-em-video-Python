n1 = int(input('Digite o primeiro número para somar: '))
n2 = int(input('Digite o segundo número para soma: '))
soma = n1 + n2
parada = 0
digitados = 2
while (parada != 999):
    parada = int(input('Digite caso queira somar mais algum número: '))
    soma = soma + parada
    digitados = digitados + 1
print('Foram digitados {}'.format(digitados - 1))
print('A soma entre eles é: {}'.format(soma - 999))
