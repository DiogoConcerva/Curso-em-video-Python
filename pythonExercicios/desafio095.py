l = []
gols = []
d = {}
while True:
    d['nome'] = input('Nome do jogador: ').capitalize()
    partidas = int(input(f'Quantas partidas {d["nome"]} jogou? '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}: ')))
    d['gols'] = gols[:]
    d['total'] = sum(gols)
    l.append(d.copy())
    gols.clear()
    opc = input('Quer continuar? [S / N] ').upper()
    if opc == 'N':
        break
print('-=' * 50)
print(f'{"Cod.":<5}{"Nome":<20}{"Gols":<30}{"Total"}')
print('-' * 100)
for c in range(len(l)):
    print(f'{c + 1:<5}{l[c]["nome"]:<20}{l[c]["gols"]}{"":<30}{l[c]["total"]}')
print('-' * 100)
while True:
    dados = int(input('Mostrar dados de qual jogador? '))
    if 1 <= dados <= len(l):
        print(f'-- LEVANTAMENTO DO JOGADOR: {l[dados - 1]["nome"]}')
        qtdJogos = len(l[dados - 1]['gols'])
        for c in range(qtdJogos):
            print(f'   No jogo {c + 1} fez {l[dados - 1]["gols"][c]} gol(s).')
        print('-' * 100)
    elif dados == 999:
        print(f'<< Volte sempre! >>')
        break
    else:
        print(f'ERRO! Não existe jogador com código {dados}! Tente novamente.')
        print('-' * 100)
