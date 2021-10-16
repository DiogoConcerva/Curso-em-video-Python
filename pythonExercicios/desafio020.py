from random import shuffle

p = input('Digite o primeiro nome: ')
s = input('Digite o segundo nome: ')
t = input('Digite o terceiro nome: ')
q = input('Digite o quarto nome: ')
lista = [p, s, t, q]
shuffle(lista)

print('A sequencia de apresentação será:')
print(lista)
