from random import randint
t = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: {t}')
maior = 0
menor = 0
for c in range(0, len(t)):
    if(t[c] > maior):
        maior = t[c]
    if(c == 0):
        menor = t[c]
    elif(t[c] < menor):
        menor = t[c]
print(f'O maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')
