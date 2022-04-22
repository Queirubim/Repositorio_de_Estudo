from random import randint
tup = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for c in tup:
    print(c, end=' ')
print(f'\nO maior numero foi: {max(tup)}')
print(f'O menor numero foi: {min(tup)}')
