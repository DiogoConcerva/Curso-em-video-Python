s = float(input('Qual o seu salário? '))
if (s <= 1250):
    print('Seu salário terá aumento de 15%, agora será de R$ {:.2f}.'.format((s * 0.15) + s))
else:
    print('Seu salário terá aumento de 10%, agora será de R$ {:.2f}.'.format((s * 0.10) + s))
