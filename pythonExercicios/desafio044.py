print('{:=^55}'.format(' Lojas da Valentina '))
v = float(input('Qual o valor do produto? R$ '))
print('=' * 55)
print('Escolha a forma de pagamento:')
print('1 - À vista (dinheiro ou cheque) com 10% de desconto')
print('2 - À vista (cartão) com 5% de desconto')
print('3 - 2 vezes no cartão sem desconto')
print('4 - 3 vezes ou mais no cartão com 20% de juros')
print('=' * 55)
o = int(input('Digite a opção do cliente: '))
print('=' * 55)

if (o == 1):
    d = v * 0.1
    print('O desconto será de R$ {:.2f}, total a pagar R$ {:.2f}.'.format(d, v - d))
    print('=' * 55)

elif (o == 2):
    d = v * 0.05
    print('O desconto será de R$ {:.2f}, total a pagar R$ {:.2f}.'.format(d, v - d))
    print('=' * 55)

elif (o == 3):
    print('Sem desconto, você vai pagar 2 parcelas de R$ {:.2f} cada.'.format(v / 2))
    print('=' * 55)

else:
    j = (v + (v * 0.2))
    print('Você vai pagar 20% de juros, o produto sairá po R$ {:.2f}.'.format(j))
    print('=' * 55)
