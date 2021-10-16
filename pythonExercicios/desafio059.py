p = float(input('Digite o primeiro valor: '))
s = float(input('Digite o segundo valor: '))
print('=' * 50)
v = (int(input('''Digite o que deseja fazer:
[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior
[ 4 ] - Novos números
[ 5 ] - Sair do programa
digite sua escolha: ''')))
print('=' * 50)
while v != 5:
      if (v == 1):
            print('{} + {} = {}'.format(p, s, p + s))
            v = 4
            print('=' * 50)

      if (v == 2):
            print('{} X {} = {}'.format(p, s, p * s))
            v = 4
            print('=' * 50)

      if (v == 3):
          if (p > s):
              print('{} é o maior número'.format(p))
              v = 4
              print('=' * 50)
          else:
              print('{} é o maior número'.format(s))
              v = 4
              print('=' * 50)

      if (v == 4):
          p = float(input('Digite o primeiro valor: '))
          s = float(input('Digite o segundo valor: '))
          print('=' * 50)
          v = (int(input('''Digite o que deseja fazer:
[ 1 ] - Somar
[ 2 ] - Multiplicar
[ 3 ] - Maior
[ 4 ] - Novos números
[ 5 ] - Sair do programa
digite sua escolha: ''')))
          print('=' * 50)

print('Saindo do programa.')
print('=' * 50)