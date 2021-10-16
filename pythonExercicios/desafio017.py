from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = hypot(co, ca)
print('Sendo o cateto oposto igual a {} e o cateto adjacente igual a {} temos a hipotenusa de {:.2f}'.format(co, ca, h))