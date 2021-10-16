import datetime

d = {}
anoAtual = datetime.datetime.today().year

nome = input('Nome: ')
d['nome'] = nome
ano = int(input('Ano de nascimento: '))
d['ano'] = anoAtual - ano
carteira = int(input('Carteira de trabalho (0 não tem): '))
if carteira == 0:
    d['ctps'] = carteira
else:
    d['ctps'] = carteira
    d['contratacao'] = int(input('Ano de contratação: '))
    d['salario'] = float(input('Salário: R$ '))
    d['aposentadoria'] = d['contratacao'] + 35 - ano
for k, v in d.items():
    print(f'{k} tem o valor {v}')