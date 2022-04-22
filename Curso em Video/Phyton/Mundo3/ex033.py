def leiaInt(msg):
    while not msg.isnumeric():
        leia = input(msg)
        if leia.isnumeric():
            return leia
        else:
            print('\033[31mErro! Digite um numero inteiro válido.\033[m')


#Principal
n = leiaInt('Digite um numero inteiro: ')
print(f'Voçê acabou de digitar o numero {n}')
