a = []
t = []
while True:
    a.append(input('Nome: '))
    a.append(float(input('Nota 1: ')))
    a.append(float(input('Nota 2: ')))
    a.append((a[1] + a[2]) / 2)
    t.append(a[:])
    a.clear()
    escolha = input('Quer continuar? [S / N] ').upper()
    if escolha == 'N':
        break
print('-=' * 40)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 40)
for c in range(len(t)):
    print(f'{c:<4}{t[c][0]:<10}{t[c][3]:>8}')
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    else:
        print(f'Notas de {t[aluno][0]} são {t[aluno][1]} e {t[aluno][2]}')
        print('-' * 40)
