from random import randint
cont = 0
escolha = ' '
print(f'''{'='*40} 
{"VAMOS JOGAR PAR OU ÍMPAR": ^40}
{'='*40}''')
while True:
    jogador = int(input('Diga um valor: '))
    while escolha not in 'PI':
        escolha = str(input('[P]Par ou [I]Ímpar ?: ')).upper()[0]
    print('-'*40)
    computador = randint(0, 10)
    v = jogador + computador
    if v % 2 == 0:
        r = 'P'
    else:
        r = 'I'
    print(f'''Você Jogou {jogador} e o computador {computador}
Total deu {jogador+computador} que é {r}
{'-'*40}''')
    if r == escolha:
        print('''Você venceu !
        Vamos Joga novamente....''')
        cont += 1
    else:
        print('Você Perdeu!')
        break
print(f'Game OVER! Você cenceu {cont} vezes.')
