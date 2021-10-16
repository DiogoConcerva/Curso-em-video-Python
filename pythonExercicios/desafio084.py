dados = list()
informacoes = []
cadastro = 0
menor = maior = 0
while True:
    cadastro += 1
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if cadastro == 1:
        maior = dados[1]
        menor = maior
    elif dados[1] > maior:
        maior = dados[1]
    elif dados[1] < menor:
        menor = dados[1]
    informacoes.append(dados[:])
    dados.clear()
    escolha = str(input('Quer continuar? [S/N] ')).upper()
    if escolha == 'N':
        break
print('=-' * 30)
print(f'Ao todo você cadastrou {cadastro} pessoas.')
print(f'O maior peso foi de {maior:.1f} Kg. Peso de ', end='')
for c in informacoes:
    if maior == c[1]:
        print(f'{c[0]}', end=' ')
print(f'\nO menor peso foi de {menor:.1f} Kg. Peso de ', end='')
for c in informacoes:
    if menor == c[1]:
        print(f'{c[0]}', end=' ')
