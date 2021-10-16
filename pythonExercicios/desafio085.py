l = [[], []]
for n in range(0, 7):
    v = int(input(f'Digite o {n+1}º valor: '))
    if v % 2 == 0:
        l[0].append(v)
    else:
        l[1].append(v)
l[0].sort()
l[1].sort()
print(f'Os valores pares digitados foram: {l[0]}')
print(f'Os valores ímpares digitados foram: {l[1]}')
