n = int(input('Digite um valor ou 999 para parar: '))
soma = 0
cont = 0
while (n != 999):
    soma = soma + n
    n = int(input('Digite um valor ou 999 para parar: '))
    cont += 1
print(f'A soma dos {cont} valores é igual a {soma}!')
