import moeda


preco = float(input('Digite o preço R$ '))
print(f'A metade de {preco} é {moeda.metade(preco):.2f}')
print(f'O dobro de {preco} é {moeda.dobro(preco):.2f}')
print(f'O aumento de 10% de {preco} é {moeda.aumento(preco):.2f}')
print(f'A redução em 13% de {preco} é {moeda.reduzir(preco):.2f}')
