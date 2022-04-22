def leiadinherio(msg):
    valido = False
    while not valido:
        leia = str(input(msg).replace(',', '.').strip())
        if leia.isalpha() or leia == '':
            print('\033[31mErro! Digite um numero válido.\033[m')
        else:
            valido = True
            return float(leia)
