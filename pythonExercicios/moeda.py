def metade(valor, formatar=False):
    if not formatar:
        v = valor / 2
        return f'{v:.2f}'
    else:
        return formatacao((valor / 2), formatar)


def dobro(valor, formatar=False):
    if not formatar:
        v = valor * 2
        return f'{v:.2f}'
    else:
        return formatacao(valor * 2, formatar)


def aumento(valor, formatar=False):
    if not formatar:
        v = valor * 1.1
        return f'{v:.2f}'
    else:
        return formatacao(valor * 1.1, formatar)


def reduzir(valor, formatar=False):
    if not formatar:
        v = valor * 0.87
        return f'{v:.2f}'
    else:
        return formatacao(valor * 0.87, formatar)


def formatacao(valor, formatar=False):
    valorFormatado = str(valor).replace('.', ',')
    if valorFormatado[-1] == '0':
        return valorFormatado + '0'
    else:
        return valorFormatado


def resumo(valor, valorAumentado, valorReduzido):
    print('-' * 50)
    print('RESULMO DO VALOR'.center(50))
    print('-' * 50)
    print('Preço analisado:', formatacao(valor))
    print('Dobro do preço:', dobro(valor, True))
    print('Metade do preço:', metade(valor, True))
    print(f'{valorAumentado}% do aumento:', formatacao(((valorAumentado / 100) * valor) + valor, True))
    print(f'{valorReduzido}% do aumento:', formatacao((valor - (valorReduzido / 100) * valor), True))
    print('-' * 50)
