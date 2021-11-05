def escreva(textoDigitada):
    tamanho = len(textoDigitada) + 6
    for c in range(tamanho):
        print('~', end='')
    print(f'\n{textoDigitada.center(tamanho)}')
    for c in range(tamanho):
        print('~', end='')


escreva(input('Digite algo: '))
