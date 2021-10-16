l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
area = l * a
print('Para pintar uma área de {:.2f} m² você vai precisar de {} litros de tinta.'.format(area, area / 2))
