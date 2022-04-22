s = 'S'
v = ns = me = ma = 0
while s in 'sS':
    v += 1
    n = int(input(f'{v}º Valor = '))
    ns += n
    s = str(input('Quer continuar ? [s/n]: ')).lower().strip()[0]
    if v == 1:
        ma = me = n
    else:
        if n > ma:
            ma = n
        if n < me:
            me = n
print(f'A media entre os {v} valores foi {ns/v:.2f}.')
print(f'O maior valor foi {ma} e o menor valor foi {me}')
