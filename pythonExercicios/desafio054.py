from datetime import date
ma = 0
me = 0
ano = date.today().year
for c in range(1, 8):
    a = int(input('Digite o {}º ano de nascimento: '.format(c)))
    if((ano - a) < 21):
        me = me + 1
    else:
        ma = ma + 1
print('Há {} menore(s) de 21 anos e {} maiore(s) de 21 anos.'.format(me, ma))

