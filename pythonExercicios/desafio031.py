d = int(input('Qual a distância da viagem em KM? '))

if (d <= 200):
    print('Sua viagem de {} KM vai custar R$ 0,50 por KM, você vai pagar um total de R$ {}'
          .format(d, (0.50 * d)))
else:
    print('Sua viagem de {} KM vai custar R$ 0,45 por KM, você vai pagar um total de R$ {}'
          .format(d, (0.45 * d)))
