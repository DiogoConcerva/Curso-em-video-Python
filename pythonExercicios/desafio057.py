s = str(input('Digite seu sexo [M / F]: ')).upper()
while (s != 'M' and s != 'F'):
    s = str(input('Valor {} inválido, digite [M / F]: '.format(s))).upper()
print('Fim.')
