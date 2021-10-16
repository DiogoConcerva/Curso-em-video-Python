l = []
d = {}

d['nome'] = input('Nome do jogador: ').capitalize()
partidas = int(input(f'Quantas partidas {d["nome"]} jogou? '))
for c in range(partidas):
    l.append(int(input(f'Quantos gols na partida {c + 1}: ')))
d['gols'] = l
d['total'] = sum(l)
print('-=' * 50)
print(d)
print('-=' * 50)
for k, v in d.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 50)
print(f'O jogador {d["nome"]} jogou {len(l)} partidas.')
for c in range(len(l)):
    print(f'\t=> Na partida {c + 1}, fez {l[c]} gol(s).')
print(f'Foi um total de {sum(l)} gol(s).')
