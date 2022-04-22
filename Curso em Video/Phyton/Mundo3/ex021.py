from datetime import date
di = dict()
di['nome'] = str(input('Nome: '))
nas = int(input('Ano de Nascimento: '))
di['idade'] = date.today().year - nas
di['ctps'] = int(input('Carteira de Trabalho (0 não tem )'))
if di['ctps'] != 0:
    di['contratação'] = int(input('Ano de Contratação: '))
    di['salário'] = int(input('Salário: '))
    ap = (di['contratação'] + 35) - nas
    di['aposentadoria'] = ap
print('=='*30)
for k, v in di.items():
    print(f' - {k} tem o valor {v}')
