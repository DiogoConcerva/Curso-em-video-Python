t = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Gratis', 'Estudar', 'Praticar', 'Trabalhar',
     'Mercado', 'Programador', 'Futuro')
for c in t:
     print(f'\nNa palavra {c.upper()} temos ', end='')
     for palavra in c:
          if palavra.lower() in 'aeiou':
               print(palavra.lower(), end=' ')
