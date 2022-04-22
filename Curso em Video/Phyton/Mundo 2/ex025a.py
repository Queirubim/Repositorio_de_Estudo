print(f'{"Fatorial":=^40}')
n = int(input('Digite um numero: '))
c = n
r = 1
while c > 0:
    print(f'{c} ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    r *= c
    c -= 1
print(r)
