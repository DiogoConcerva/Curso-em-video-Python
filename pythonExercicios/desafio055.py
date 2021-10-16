ma = 0
me = 0
for c in range(1, 6):
    n = float(input('Digite o {}º peso em Kg: '.format(c)))
    if c == 1:
        ma = n
        me = n
    if(n > ma):
        ma = n
    if(n < me):
        me = n
print('O maior peso em Kg foi {} e o menor foi {}.'.format(ma, me))
