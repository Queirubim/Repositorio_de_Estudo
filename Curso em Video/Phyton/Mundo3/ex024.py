jogadores = list()
di = dict()
dados = list()
while True:
    tot = 0
    di['nome'] = str(input('Nome do Jogador: ')).capitalize()
    partidas = int(input(f'Quantas Partidas {di["nome"]} jogou ? '))
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {c+1}: '))
        tot += gols
        dados.append(gols)
    di['gols'] = dados[:]
    di['total'] = tot
    jogadores.append(di.copy())
    dados.clear()
    di.clear()
    stop = str(input('Quer continuar [S/N]: '))
    if stop in 'nN':
        break
print('=='*27)
print(f'{"N°":^3}{"NOME":<10}{"GOLS":<10}{"TOTAL"}')
print('=='*27)
for v, i in enumerate(jogadores):
    print(f'{v}  {i["nome"]}     {i["gols"]}.  {i["total"]}')
print('=='*27)
while True:
    stop = int(input('Mostrar dados de qual jogador? '))
    if stop == 999:
        break
    if stop <= len(jogadores)-1:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[stop]["nome"].upper()}:')
        for v, c in enumerate(jogadores[stop]['gols']):
            print(f'    No jogo {v+1} fez {c} gols.')
    else:
        print('Jogador inexistente tente novamente:')
