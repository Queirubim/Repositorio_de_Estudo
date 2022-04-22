def leiaInt(msg):
    while True:
        try:
            leia = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um numero inteiro válido.\033[m')
            continue
        else:
            return leia


def leiafloat(msg):
    while True:
        try:
            leia = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um numero real válido.\033[m')
        else:
            return leia


i = leiaInt('Digite um numero Inteiro: ')
r = leiafloat('Digite um numero Real: ')
print(f'O valor inteiro digitado foi {i} e o real {r}')
