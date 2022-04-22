print(f'{"Fatorial":=^40}')
n = int(input('Diga um numeor: '))
c = n
f = 1
for r in range(1, n+1):
    if c > 0:
        print(f'{c}', end='')
        print(' x ' if c > 1 else ' = ', end='')
        f *= c
        c -= 1
print(f'{f}')
