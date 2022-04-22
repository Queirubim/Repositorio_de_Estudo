from random import randint
from time import sleep
numal = randint(0, 5)
nump = int(input('Digite um numero de 0 á 5 : '))
print('Pensando.....')
sleep(3)
if numal == nump:
    print('Voçê Ganhou !')
else:
    print('Voçê Perdeu!')
print(f'O numero que Voce escolheu foi: {nump} e o numero sorteado foi: {numal}.')
print('fim')
