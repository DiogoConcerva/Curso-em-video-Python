print('=' * 50)
print('BANCO DAC'.center(50))
print('=' * 50)
v = int(input('Qual valor você deseja sacar R$: '))
print('=' * 50)
print()
while(v != 0):
    if(v >= 50):
        d = v // 50
        print(f'Total de {d} de cédulas de R$ 50,00')
        d = v - (d * 50)
        v = d
    if(v >= 20):
        d = v // 20
        print(f'Total de {d} de cédulas de R$ 20,00')
        d = v - (d * 20)
        v = d
    if (v >= 10):
        d = v // 10
        print(f'Total de {d} de cédulas de R$ 10,00')
        d = v - (d * 10)
        v = d
    if (v >= 1):
        print(f'Total de {d} de cédulas de R$ 1,00')
    break
print()
print('=' * 50)
print('Volte sempe ao Banco DAC! Tenha um bom dia.')
