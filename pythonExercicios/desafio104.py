def leiaInt(numero):
    validacao = False
    valor = 0
    while True:
        num = str(input(numero))
        if num.isnumeric():
            valor = int(num)
            validacao = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if validacao:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
