km = float(input('Quantos KM você percorreu? '))
d = int(input('Quantos dias você ficou com o carro? '))
v = (0.15 * km) + (60 * d)
print('Você ficou {} dias com o carro e percorreu uma distância de {} KM, valor a pagar R$: {:.2f}'.format(d, km, v))
