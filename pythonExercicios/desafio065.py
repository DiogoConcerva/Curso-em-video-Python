n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = n1 + n2
contador = 2
media = soma / contador
if (n1 > n2):
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
p = str(input('Você deseja continuar? [S / N]: ')).upper()
while (p == 'S'):
    n3 = int(input('Digite um número: '))
    soma = soma + n3
    contador = contador + 1
    media = soma / contador
    if (n3 > maior):
        maior = n3
    elif (n3 < menor):
        menor = n3
    p = str(input('Você deseja continuar? [S / N]: ')).upper()
print('A média entre todos os números digitados foi: {}'.format(media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
