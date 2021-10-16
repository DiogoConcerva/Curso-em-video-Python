l = []
d = {}
somaIdade = 0
while True:
    d['nome'] = input('Nome: ').capitalize()
    d['sexo'] = input('Sexo [M / F]: ').upper()
    d['idade'] = int(input('Idade: '))
    somaIdade += d['idade']
    l.append(d.copy())
    esc = input('Desaja continuar [S / N]? ')
    if esc in 'Nn':
        break
mediaIdade = somaIdade / len(l)
print('-=' * 30)
print(f'- O grupo tem {len(l)} pessoas.')
print(f'- A média de idade é de {mediaIdade:.2f} ano(s).')
print(f'- As mulheres cadastradas foram: ', end='')
for c in range(len(l)):
    if l[c]['sexo'] == 'F':
        print(f'{l[c]["nome"]} ', end='')
print(f'\n- Lista das pessoas que estão acima da média:')
for c in range(len(l)):
    if l[c]['idade'] > mediaIdade:
        print(f'Nome: {l[c]["nome"]}, Sexo: {l[c]["sexo"]} e Idade: {l[c]["idade"]}')
print('-=' * 30)
