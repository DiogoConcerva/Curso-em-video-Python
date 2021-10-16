n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if (media == 5.0):
    print('\033[31mREPROVADO, sua média foi {} estude mais.\033[m'.format(media))
elif ((media > 5.0) and (media < 6.9)):
    print('\033[33mVocê está em RECUPERAÇÃO, sua média foi {}\033[m'.format(media))
else:
    print('\033[36mCurta suas férias você esta APROVADO, sua média foi {}\033[m'.format(media))
