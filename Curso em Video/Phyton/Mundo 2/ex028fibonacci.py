ta = 0
th = 1
n = 0
print('~'*30)
print(f'{"SEQUENCIA DE FIBONACCI": ^30}')
print('~'*30)
v = int(input('Quantos termos voçê quer ver ?: '))
while v != n:
    print(f'{th} => ', end='')
    th += ta
    ta = th - ta
    n += 1
print('FIM DA SEQUENCIA')
