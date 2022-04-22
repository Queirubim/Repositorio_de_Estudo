n = ('Maconha', 100, 'Bala', 30, 'Maçã', 1.50,
     'Vodka', 29.90, 'ICE', 2.30, 'Tekila', 50,
     'Maminha', 40.99, 'Picanha', 59, 'File', 45.50)
print(f'''{"-"*44}
{"O GRANDE CHURRASCO": ^44}
{"-"*44}''')
for c in range(0, len(n)):
    if c % 2 == 0:
        print(f'{n[c]:.<35}R$ {n[c+1]: >6.2f}')
print('-'*44)
