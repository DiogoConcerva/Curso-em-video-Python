l = []
m = []
somaPares = maiorValor = 0

for c in range(3):
    for x in range(3):
        l.append(int(input(f'Digite um valor para [{c}, {x}] ')))
    if c == 1 and x < 3:
        maiorValor = max(l)
    m.append(l[:])
    l.clear()
print('=-' * 30)
for c in range(3):
    for x in range(3):
        print(f'[  {m[c][x]}  ]', end='')
        if m[c][x] % 2 == 0:
            somaPares += m[c][x]
    print()
print('=-' * 30)
print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {m[0][2] + m[1][2] + m[2][2]}')
print(f'O maior valor da segunda linha é {maiorValor}')
