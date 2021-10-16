from time import sleep
print('=' * 50)
print('DIOGO IMPORTADOS'.center(50))
print('=' * 50)
continuar = 'S'
total = 0
maisMil = 0
cont = 0

while(continuar == 'S'):
    nome = str(input('Nome do produto: '))
    preco = float(input('Digite o valor do produto - R$: '))
    total = total + preco
    cont += 1
    if(preco > 1000):
        maisMil += 1
    if cont == 1:
        precoBarato = preco
        maisBarato = nome
    else:
        if(preco < precoBarato):
            precoBarato = preco
            maisBarato = nome
    continuar = str(input('Deseja continuar [S / N]: ')).strip().upper()
    while(continuar != 'S' and continuar != 'N'):
        continuar = str(input('Deseja continuar [S / N]: ')).strip().upper()
    print('=' * 50)
print('FIM DO PROGRAMA - CALCULANDO')
sleep(2)
print(f'Total gastos nas compras R$: {total:.2f}')
print(f'Quantos produtos custam mais de R$ 1.000,00: {maisMil}')
print(f'O produto mais barato é o(a) {maisBarato}')
print('=' * 50)
