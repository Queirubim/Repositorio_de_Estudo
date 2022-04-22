from random import randint
from time import sleep
print(f'''\033[34m{"JOKENPO":~^40}\033[m
>>>0<<<   PEDRA
>>>1<<<   PAPEL
>>>2<<<   TESOURA''')
itens = ('PEDRA', 'PAPEL', 'TESOURA')
jogador = int(input('Qual sua escolha : '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
comp = randint(0, 2)
print('Voçê', end=' ')
if comp == 0:
    if jogador == 0:
        print('\033[33mEMPATOU !!!')
    elif jogador == 1:
        print('\033[32mVENCEU !!!')
    elif jogador == 2:
        print('\033[31mPERDEU !!!')
    else:
        print('Voce fez um jogada\033[31m INVALIDA !!!')
elif comp == 1:
    if jogador == 0:
        print('\033[31mPERDEU !!!')
    elif jogador == 1:
        print('\033[33mEMPATOU !!!')
    elif jogador == 2:
        print('\033[32mVENCEU !!!')
    else:
        print('Voce fez um jogada\033[31m INVALIDA !!!')
elif comp == 2:
    if jogador == 0:
        print('\033[31mPERDEU !!!')
    elif jogador == 1:
        print('\033[32mVENCEU !!!')
    elif jogador == 2:
        print('\033[33mEMPATOU !!!')
    else:
        print('Voce fez um jogada\033[31m INVALIDA !!!')
print('><' * 12)
print(f'O jogador jogou {itens[jogador]} !')
print(f'O computador jogou {itens[comp]} !')
print('><' * 12)
