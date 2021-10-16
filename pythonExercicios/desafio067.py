n = int(input('Quer ver a tabuada de qual valor? '))
print('-' * 45)
while (n >= 0):
    for cont in range(1, 11, +1):
        print(n, 'X', cont, ' = ', n * cont)
    print('-' * 45)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 45)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
