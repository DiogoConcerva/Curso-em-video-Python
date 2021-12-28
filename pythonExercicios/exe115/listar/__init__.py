def listarInformacoes():
    print('-' * 55)
    print('PESSOAS CADASTRADAS'.center(55))
    print('-' * 55)
    try:
        with open('contatos.txt', 'r') as arq:
            for line in arq:
                nome = line.split(';')[0]
                idade = line.split(';')[1].rstrip('\n')
                print(f'{nome:<47}{idade:>3} anos')
    except:
        print('\033[1;31mErro ao carregar informações!!\033[m')
