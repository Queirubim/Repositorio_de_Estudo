t1 = int(input('DIGITE UM TERMO: '))
ra = int(input('RAZÂO: '))
pro = t1
c = 1
t = 0
mais = 10
while mais != 0:
    t = t + mais
    while c <= t:
        print(f'{pro} => ', end='')
        pro += ra
        c += 1
    print('Pausa')
    t = int(input('\nQuer ver mais quantos termos: '))
print(f'A progresão foi finalizada com {t} termos.')
