def dobro(a, p=False):
    b = a * 2
    return b if not p else moeda(b)


def metade(a, p=False):
    b = a / 2
    return b if not p else moeda(b)


def aumentar(a, b, p=False):
    c = (a / 100) * b + a
    return c if p is False else moeda(c) #is = '=='


def diminuir(a, b, p=False):
    c = a - (b / 100) * a
    return c if p is False else moeda(c)


def moeda(a):
    return f'R${a:.2f}'.replace('.', ',')


def resumo(a, au, re):
    print('-'*30)
    print(f'{"RESUMO DO VALOR": ^30}')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(a)}')
    print(f'Dobro do preço: \t{dobro(a, True)}')
    print(f'Metade do preço: \t{metade(a, True)}')
    print(f'{au}% de aumento: \t{aumentar(a, au, True)}')
    print(f'{re}% de redução: \t{diminuir(a, re, True)}')
    print('-'*30)


def leiaInt(msg):
    while not msg.isnumeric():
        leia = input(msg)
        if leia.isnumeric():
            return int(leia)
        else:
            print('\033[31mErro! Digite um numero inteiro válido.\033[m')


def forma(msg):
    print('='*40)
    print(msg.center(40))
    print('='*40)


def adicionar():
    forma('NOVO CADASTRO')
    arquivo = open("texto.txt", "a")
    nome = str(input('Nome: '))
    idade = leiaInt('Idade: ')
    arquivo.write(f'{nome}   {idade}\n')
    print(f'Novo arquivo de {nome} adicionado.')
    arquivo.close()


def menu():
    forma('MENU PRINCIPAL')
    print(f'''\033[33m1\033[m - \033[34mVer pessoas cadastradas\033[m
\033[33m2\033[m - \033[34mCadastrar nova Pessoa\033[m
\033[33m3\033[m - \033[34mSair do Sistema\033[m
{'=' * 40}''')
