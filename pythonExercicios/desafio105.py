def notas(*notas, sit=False):
    relatorio = {}
    """
    -> Função para análisar notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    maior = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    if not sit:
        relatorio = {'Quantidade de notas': len(notas), 'Maior nota': maior, 'Menor nota': menor, 'Média da turma': media}
    else:
        if media <= 5:
            relatorio = {'Quantidade de notas': len(notas), 'Maior nota': maior, 'Menor nota': menor,
                         'Média da turma': media, 'Situação': 'Ruim'}
        elif 5 < media < 7.0:
            relatorio = {'Quantidade de notas': len(notas), 'Maior nota': maior, 'Menor nota': menor,
                         'Média da turma': media, 'Situação': 'Razoável'}
        else:
            relatorio = {'Quantidade de notas': len(notas), 'Maior nota': maior, 'Menor nota': menor,
                         'Média da turma': media, 'Situação': 'Boa'}
    return relatorio


informacoes = notas(5, 6.8, 10, 7, sit=True)
print(informacoes)
#help(notas)
