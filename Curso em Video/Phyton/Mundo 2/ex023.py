from random import randint
numal = randint(0, 10)
acertou = False
print('='*60)
print(f'{"Estou pensando em um numero de 0 a 10 tente advinhar": ^60}')
print('='*60)
p = 0
while not acertou:
    nump = int(input('Em que numero estou pensando ?: '))
    p += 1
    if nump == numal:
        acertou = True
    if nump > numal:
        print('Um pouco menos')
    elif nump < numal:
        print('Um pouco mais')
print(f'Foram nescesarios {p} Palpites para acertar seu resultado.')
