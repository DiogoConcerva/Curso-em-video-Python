t = int(input('Digite o número para tabuada que você deseja estudar: '))
i = int(input('Até que número você deseja estudar: '))
for c in range(0, i + 1):
    print('{} X {} = {}'.format(c, t, c * t))
