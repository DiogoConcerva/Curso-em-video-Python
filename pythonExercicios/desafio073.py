t = ('Náutico', 'Coritiba', 'Guarani', 'CRB', 'Goiás', 'Sampaio Corrêa', 'Avaí', 'Vasco da Gama', 'Operário', 'Brusque',
     'CSA', 'Vila Nova', 'Botafogo', 'Remo', 'Brasil de Pelotas', 'Cruzeiro', 'Confiança', 'Vitória', 'Ponte Preta', 'Londrina')
print(f'A lista de times do Brasileirão Série B são: {t}')

print('Os 5 primeiros colocados são:')
for c in range(0, 5):
    print(t[c])
print('Os últimos 4 colocados são:')
for c in range(16, 20):
    print(t[c])
print('Os times em ordem alfabética:')
print(sorted(t))
print('Em que posição na tebela está o Brusque:')
print(f'O Náutico esta na {t.index("Brusque")+1}ª posição.')
