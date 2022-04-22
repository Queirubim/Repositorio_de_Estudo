lista = list()
di = dict()
s = 0
while True:
    di['nome'] = str(input('Nome: ')).capitalize()
    di['sexo'] = str(input('Sexo [M/F]: ')).upper()
    di['idade'] = int(input('Idade: '))
    lista.append(di.copy())
    di.clear()
    stop = str(input('Quer continuar [S/N]: '))
    if stop in 'Nn':
        break
print('='*30)
print(f'Ao todo foram cadastradas {len(lista)} pessoas.')
print(f'As mulheres do grupo foram:', end=' ')
for i in lista:
    s += i['idade']
    if i['sexo'] == 'F':
        print(i['nome'], end=' ')
print(f'\nA media das idades foi de {s/len(lista)} anos.')
print(f'A lista de pessoas que estão acima da média: ')
for i in lista:
    if i['idade'] > s/len(lista):
        print(f'nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]}...')
print('ENCERRADO')
