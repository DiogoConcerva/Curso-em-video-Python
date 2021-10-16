t = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
print('=' * 60)
print('A sequencia solicitada é:')
print('=' * 60)
for c in range(1, 11):
    print('{}º - {}'.format(c, t))
    t = t + r
print('=' * 60)
