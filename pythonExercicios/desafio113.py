def leiaInt(numero):
    while True:
        try:
            num = int(input(numero))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return num


def leiaFloat(numero):
    while True:
        try:
            num = float(input(numero))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return num


inteiro = leiaInt('Digite um número: ')
real = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
