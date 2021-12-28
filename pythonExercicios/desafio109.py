import moeda


preco = float(input('Digite o preço R$ '))
print(f'A metade de R$ {moeda.formatacao(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de R$ {moeda.formatacao(preco)} é {moeda.dobro(preco)}')
print(f'O aumento de 10% de R$ {moeda.formatacao(preco)} é {moeda.aumento(preco, True)}')
print(f'A redução em 13% de R$ {moeda.formatacao(preco)} é {moeda.reduzir(preco)}')
