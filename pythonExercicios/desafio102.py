def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número
    :para n: O número a ser calculado
    :para show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n.
    """
    fat = 1
    for c in range(numero, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat


#help(fatorial)
print(fatorial(5, show=True))
