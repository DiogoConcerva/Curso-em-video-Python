t = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'Você digitou os valores: {t}')
posicao = 0
pares = 0
print(f'O valor 9 apareceu {t.count(9)} vez(es)')
if 3 in t:
    print(f'O valor 3 apareceu na {t.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os números pares digitados foram: ', end='')
for c in t:
    if c % 2 == 0:
        print(c, end=' ')
