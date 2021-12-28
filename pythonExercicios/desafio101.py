def voto(ano):
    import datetime
    anoAtual = datetime.datetime.now().year
    idade = anoAtual - ano
    if idade >= 16 and idade <= 17 or idade >= 70:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade >= 18 and idade < 70:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    else:
        return f'Com {idade} anos: NÃO VOTA.'


print('------------------------------------------')
print(voto(int(input('Em que ano você nasceu? '))))
