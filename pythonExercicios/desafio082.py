opcao = 'S'
l = []
p = []
i = []
while(opcao == 'S'):
    n = int(input('Digite um número: '))
    l.append(n)
    opcao = str(input('Quer continua? [S/N] ')).upper()
print('=-' * 30)
print(f'A lista completa é {l}')
for c in range(len(l)):
    if(l[c] % 2 == 0):
        p.append(l[c])
    else:
        i.append(l[c])
print(f'A lista de pares é {p}')
print(f'A lista de ímapres é {i}')
