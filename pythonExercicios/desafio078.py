lista = []
for c in range(0, 5):
    n = int(input(f'Digite um valor para posição {c}: '))
    lista.insert(c, n)
print('=-' * 40)
maior = max(lista)
menor = min(lista)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} na(s) posição(ões) ', end='')
for pos in range(len(lista)):
    if(maior == lista[pos]):
        print(f'{pos}... ', end=' ')
print(f'\nO menor valor digitado foi {menor} na(s) posição(ões) ', end='')
for pos in range(len(lista)):
    if(menor == lista[pos]):
        print(f'{pos}... ', end=' ')
