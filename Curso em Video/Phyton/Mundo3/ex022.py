di = dict()
dados = list()
di['nome'] = str(input('Nome do Jogador: ')).capitalize()
partidas = int(input(f'Quantas Partidas {di["nome"]} jogou ? '))
for c in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {c+1}: '))
    dados.append(gols)
di['gols'] = dados[:]
di['total'] = sum(dados)
print('=='*27)
print(di)
print('=='*27)
for k, v in di.items():
    print(f'O campo {k} tem o valor {v}.')
print('=='*27)
print(f'O Jogador {di["nome"]} jogou {len(di["gols"])} partidas.')
for c, v in enumerate(di['gols']):
    print(f'    => Na Partida {c+1}, fez {v} gols.')
print(f'Foi um total de {di["total"]} gols.')
