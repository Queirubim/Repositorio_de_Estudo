from random import randint
from operator import itemgetter
jogadas = dict()
rank = list()
print('Valores Sorteados:')
for c in range(0, 6):
    dados = randint(1, 6)
    jogadas[f'Jogador {c+1}'] = dados
    print(f'    O jogador {c+1} tirou {dados}')
rank = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('Valores em Ordem')
for v, c in enumerate(rank):
    print(f'    {v+1} lugar {c[0]} com {c[1]}.')
