t1 = int(input('Primeiro termo: '))
ra = int(input('Razão: '))
c = 0
while c != 10:
    pro = t1 + c * ra
    c += 1
    print(f'{pro} ->', end='')
print(' fim')
