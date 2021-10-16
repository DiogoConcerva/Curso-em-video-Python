from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))
anoCorrente = date.today()
categoria = anoCorrente.year - ano

if (categoria <= 9):
    print('Nadadaor da categoria MIRIM, sua idade atua é de {} anos.'.format(categoria))
elif (categoria <= 14):
    print('Nadador da categoria INFANTIL, sua idade atual é de {} anos.'.format(categoria))
elif (categoria <= 19):
    print('Nadador da categoria JUNIOR, sua idade atual é de {} anos.'.format(categoria))
elif (categoria <= 20):
    print('Nadador da categoria SÊNIOR, sua idade atual é de {} anos.'.format(categoria))
else: print('Nadador da categoria MASTER, sua idade atual é de {} anos.'.format(categoria))
