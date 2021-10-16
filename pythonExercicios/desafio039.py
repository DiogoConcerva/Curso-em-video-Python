from datetime import date
ano = int(input('Digite o ano de seu nascimento: '))
anoAtual = date.today()
tempo = anoAtual.year - ano
if (tempo == 18):
    print('Está na hora do seu alistamento')
elif (tempo < 18):
    print('Faltam {} anos para o seu alistamento.'.format(18 - tempo))
else:
    print('O seu prazo de alistamento passou em {} anos.'.format(tempo - 18))
