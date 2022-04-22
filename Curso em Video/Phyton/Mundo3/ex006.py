vog = ('Casa', 'Telhado', 'Teto', 'Maçaneta', 'Porta', 'Piso', 'Parede', 'Lampada')
for c in vog:
    print(f'\nNa palavra {c.upper()} encontrase as vogais ', end='')
    for d in c:
        if d in 'aeiou':
            print(d, end=' ')
