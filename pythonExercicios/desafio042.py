l1 = float(input('Digite o valor do primeiro lado do triângulo: '))
l2 = float(input('Digite o valor do segundo lado do triângulo: '))
l3 = float(input('Digite o valor do terceiro lado do triângulo: '))
print('=' * 50)
if ((l1 < l2 + l3) and (l2 < l1 + l3) and (l3 < l1 + l2)):
    print('Os segmentos podem formar um triângulo.')
    print('=' * 50)
    if (l1 == l2 == l3):
        print('O triângulo formado é um Equilátero')
        print('=' * 50)

    elif ((l1 == l2) or (l1 == l3) or (l2 == l3)):
        print('O triângulo formado é um Isósceles')
        print('=' * 50)

    elif (l1 != l2 != l3):
        print('O triângulo formado é um Escaleno')
        print('=' * 50)

else:
    print('O segmento não pode formar um triângulo.')
    print('=' * 50)
