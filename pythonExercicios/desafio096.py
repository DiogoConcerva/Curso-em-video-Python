def area(largura, comprimento):
    print(f'A área de um terreno {largura} X {comprimento} é de {largura * comprimento}m².')
    print('-' * 50)


print('Controle de terrenos')
print('-' * 50)
area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))
