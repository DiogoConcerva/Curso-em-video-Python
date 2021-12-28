def ficha(nome='', gols=''):
    if nome.strip() == '':
        if gols.strip().isnumeric() == '':
            return f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.'
        else:
            return f'O jogador <desconhecido> fez 0 gol(s) no campeonato.'
    elif nome != '':
        if gols.strip().isnumeric() == '':
            return f'O jogador {nome} fez {gols} gol(s) no campeonato.'
        else:
            return f'O jogador {nome} fez 0 gol(s) no campeonato.'


nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
print(ficha(nome, gols))
