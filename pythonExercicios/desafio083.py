msg = str(input('Digite a expressão: '))
l = list()
for c in msg:
    if c == '(':
        l.append('(')
    elif c == ')':
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')
            break
if len(l) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')
