def cadastro():
    print('-' * 55)
    print('NOVO CADASTRO'.center(55))
    print('-' * 55)
    nome = input('Nome: ')
    while True:
        idade = input('Idade: ')
        if idade.isnumeric():
            break
        else:
            print('\033[1;31mERRO: Digite um valor inteiro válido!\033[m')

    try:
        with open('contatos.txt', 'a') as arq:
            arq.write(nome + ';')
            arq.write(idade + '\n')
    except:
        print('\033[1;31mErro ao salvar informações!!\033[m')
    else:
        print(f'Novo registro de {nome} adicionado.')

