s = 0
for c in range(1, 7):
    a = int(input('Digite o {}º número: '.format(c)))
    print('=' * 35)
    if ((a % 2) == 0):
        s = s + a
print('A soma dos números pares é: {}'.format(s))
print('=' * 35)