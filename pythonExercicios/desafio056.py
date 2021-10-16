mi = 0
idade = 0
nomeVelho = ''
idadeVelho = 0
totalMulheres = 0
for c in range(1,5):
    print('----- {}ª PESSOA -----'.format(c))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    idade += i
    s = str(input('Sexo [F/M]: ')).strip().upper()
    print('=' * 40)
    if c == 1 and s in 'M':
        nomeVelho = n
        idadeVelho = i
    if s in 'M' and i > idadeVelho:
        nomeVelho = n
        idadeVelho = i
    if s in 'F' and i < 20:
        totalMulheres += 1
print('A média de idade é de {:.1f} anos.'.format(idade / 4))
print('O homem mais velho é {} com {} de idade.'.format(nomeVelho, idadeVelho))
print('O total de mulheres com menos de 20 anos é igual a {}.'.format(totalMulheres))