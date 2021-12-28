def leiaDinheiro(preco):
    validacao = False
    while not validacao:
        entrada = str(input(preco)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválifo.\033[m')
        else:
            validacao = True
            return float(entrada)
