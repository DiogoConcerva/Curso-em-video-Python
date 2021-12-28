from exe115 import cadastrar
from exe115 import listar
from time import sleep


while True:
    try:
        print('-' * 55)
        print('MENU PRINCIPAL'.center(55))
        print('-' * 55)
        print('\033[1;33m1 -\033[m \033[1;34mVer pessoas cadastradas\033[m')
        print('\033[1;33m2 -\033[m \033[1;34mCadastrar nova pessoa\033[m')
        print('\033[1;33m3 -\033[m \033[1;34mSair do sistema\033[m')
        print('-' * 55)
        escolha = int(input('\033[1;33mSua opção: \033[m'))
        if escolha < 1 or escolha > 3:
            print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    except:
        print('\033[1;31mERRO! Você deve escolher entre as opções 1, 2, ou 3\033[m')
    else:
        if escolha == 1:
            sleep(2)
            listar.listarInformacoes()
        elif escolha == 2:
            sleep(2)
            cadastrar.cadastro()
        elif escolha == 3:
            sleep(2)
            print('-' * 55)
            print('Saindo do sistema... Até logo!'.center(55))
            print('-' * 55)
            break
