from time import sleep


def cont(a, b, c):
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print('=='*18)
    print(f'Contagem de {a} ate {b} de {c} em {c}.')
    con = a
    if a > b:
        while con >= b:
            print(con, end=' ')
            sleep(0.5)
            con -= c
    else:
        while con <= b:
            print(con, end=' ')
            sleep(0.5)
            con += c
    print('Fim !')


cont(1, 10, 1)
cont(10, 0, 2)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
cont(i, f, p)
