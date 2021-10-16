l = []
m = []
for c in range(3):
    for x in range(3):
        l.append(int(input(f'Digite um valor para [{c}, {x}] ')))
    m.append(l[:])
    l.clear()
print('=-' * 30)
for c in range(3):
    for x in range(3):
        print(f'[  {m[c][x]}  ]', end='')
    print()
