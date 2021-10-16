frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntas = ''.join(palavras)
inverso = ''
for c in range(len(juntas) - 1, -1, -1):
    inverso = inverso + juntas[c]
if(inverso == frase):
    print('A frase {} é um palíndromo, pois seu inverso é {}'.format(juntas, inverso))
else:
    print('A frase {} não é um palíndromo, pois seu inverso é {}'.format(juntas, inverso))
