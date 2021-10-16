l = []
opcao = 'S'
while(opcao == 'S'):
    n = int(input('Digite um valor: '))
    l.append(n)
    opcao = str(input('Quer continuar? [S/N] ')).upper()
print('=-' * 30)
print(f'Você digitou {len(l)} elementos')
l.sort(reverse=True)
print(f'Os valores em ordem decrescente são {l}')
if 5 in l:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')