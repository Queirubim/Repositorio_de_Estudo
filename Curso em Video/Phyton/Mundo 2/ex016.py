t1 = int(input('Primeiro termo: '))
ra = int(input('Diga a razão: '))
for c in range(0, 10):
    pro = t1 + c * ra
    print(f'{pro} -> ', end='')
print('FIM')
