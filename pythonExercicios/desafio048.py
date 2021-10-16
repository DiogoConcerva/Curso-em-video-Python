s = 0
print('=' * 50)
print('Os números múltiplos de 3 entre entre 1 e 500 são:')
print('=' * 50)
for c in range(1, 501):
    if (c % 3 == 0):
        print(c)
        if ((c % 2 != 0)):
            s = s + c
print('=' * 56)
print('A soma de todos os números ímpares entre 1 e 500 é {}'.format(s))
print('=' * 56)
