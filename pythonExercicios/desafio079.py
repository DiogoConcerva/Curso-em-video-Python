lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    if opcao == 'N':
        break
print('=-' * 20)
lista.sort()
print(f'Você digitou os valores {lista}')

