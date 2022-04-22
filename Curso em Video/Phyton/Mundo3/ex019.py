aluno = dict()
aluno['Nome'] = str(input('Nome: ')).capitalize()
aluno['Media'] = float(input(f'Media de {aluno["Nome"]}: '))
if aluno['Media'] >= 7:
    aluno['Estado'] = 'Aprovado'
else:
    aluno['Estado'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
