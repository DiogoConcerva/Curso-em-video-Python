print('=' * 40)
c1 = float(input('Digite o comprimento da primeira reta: '))
c2 = float(input('Digite o comprimento da segunda reta: '))
c3 = float(input('Digite o comprimemto da terceira reta: '))
if (c1 < c2 + c3) and (c2 < c1 + c3) and (c3 < c1 + c2):
    print('Os segmentos podem formar um triângulo.')
else:
    print('Os segmentos não podem formar um triângulo.')
