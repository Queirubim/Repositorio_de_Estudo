from random import randint
from time import sleep
jogos = list()
dados = list()
d = 0
print('-'*30)
print(f'{"JOGA NA MEGA SENA": ^30}')
print('-'*30)
q_jogos = int(input('Quantos Jogos você quer que eu sortei? '))
print(f'====== Sorteando {q_jogos} JOGOS ======')
for c in range(0, q_jogos):
    while len(dados) != 6:
        d = (randint(1, 60))
        if d not in dados:
            dados.append(d)
    jogos.append(dados[:])
    dados.clear()
    jogos[c].sort()
    print(f'Jogo {c+1}: {jogos[c]}')
    sleep(1)
print('==========<BOA SORTE>==========')
