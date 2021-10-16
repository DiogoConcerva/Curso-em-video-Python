maiorIdade = 0
mulheres = 0
homens = 0
continuar = 'S'
print('-' * 50)

while continuar == 'S':
    print('CADASTRAR UMA PESSOA')
    print('-' * 50)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M / F] ')).strip().upper()
    while(sexo != 'M' and sexo != 'F'):
        sexo = str(input('Sexo: [M / F] ')).strip().upper()
    if (idade > 18):
        maiorIdade = maiorIdade + 1
    if (sexo == 'M'):
        homens += 1
    if (sexo == 'F' and idade < 20):
        mulheres += 1
    print('-' * 50)
    continuar = str(input('Quer continuar? [S / N] ')).strip().upper()
    while (continuar != 'S' and continuar != 'N'):
        continuar = str(input('Quer continuar? [S / N] ')).strip().upper()
    print('-' * 50)
print('FIM DO PROGRAMA')
print('-' * 50)
print(f'São maiores de 18 anos {maiorIdade} pessoa(s).')
print(f'Foram cadastrados {homens} homen(s).')
print(f'Tem {mulheres} mulhere(s) com menos de 20 anos.')
