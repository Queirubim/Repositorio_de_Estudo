alunos = list()
dados = list()
notas = list()
while True:
    nome = str(input('Nome: '))
    n1 = int(input('Nota 1: '))
    n2 = int(input('Nota 2: '))
    m = (n2 + n1)/2
    alunos.append([nome, [n1, n2], m])
    stop = str(input('Quer continuar? [S/N]: '))
    if stop in 'Nn':
        break
print('='*30)
print(f'{"No.":<3}{"NOME":<12}{"MÉDIA":^12}')
print('='*30)
for v, a in enumerate(alunos):
    print(f'{v:<3}{alunos[v][0]:<12}{alunos[v][2]:^12}')
print('='*30)
while True:
    n1 = int(input('Mostrar as notas de qua aluno? (999 Interrompe): '))
    if n1 == 999:
        break
    if n1 <= len(alunos) - 1:
        print(f'Notas de {alunos[n1][0]} são {alunos[n1][1]}')
