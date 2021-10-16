v = float(input('Qual a velocidade do carro em KM? '))
m = v - 80
if (v > 80):
    print('Você foi multado, a multa é de R$ 7,00 por cada KM acima do limite')
    print('Você ultrapassou em {} KM e vai pagar R$ {}.'.format((m), (7 * m)))
else:
    print('Parabéns, você respeita o limite de velocidade.')