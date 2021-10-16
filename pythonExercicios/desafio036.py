vc = float(input('\033[30;42m Qual o valor da casa:\033[m '))
s = float(input('\033[30;42m Qual o salário do comprador: \033[m '))
a = int(input('\033[30;42m Quantos anos para pagar: \033[m '))

np = a * 12
p = vc / np

if (p <= (s * 0.3)):
    print('\033[36m Emprestimo liberado! Parabéns. Sua parcela sera de R$ {:.2f} em {} prestações.\033[m'.format(p, np))
else:
    print('\033[31m Seu empréstimo não pode ser liberado.\033[m')
