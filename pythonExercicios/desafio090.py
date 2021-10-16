d = {}
d['nome'] = input('Nome: ')
d['nota'] = float(input(f'Média de {d["nome"]}: '))
print(f'Nome é igual a {d["nome"]}')
print(f'Média é igual a {d["nota"]}')
if d['nota'] >= 7.0:
    print('Situação é igual Aprovado')
else:
    print('Situação é igual Reprovado')