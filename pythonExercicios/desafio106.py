def ajuda(escolha):
    print('\033[44m~' * 50)
    print(f"Acessando o manual do comando '{escolha}'".center(50))
    print('~' * 50)
    print('\033[m')
    print('\033[7;40m')
    return f'{help(escolha)}'


while True:
    print('\033[m')
    print('\033[42m~' * 50)
    print('SISTEMA DE AJUDA PyHELP'.center(50))
    print('~' * 50)
    entrada = input('\033[mFunção ou Biblioteca: ').lower()
    if entrada == 'fim':
        #laco = False
        print('\033[41m~' * 50)
        print('ATÉ LOGO!'.center(50))
        print('~' * 50)
        break
    else:
        ajuda(entrada)
