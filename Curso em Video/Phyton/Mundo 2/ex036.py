print(f'''{'='*30}
{"BANCO": ^30}
{'='*30}''')
sacar = int(input('Que Valor Quer Sacar ? R$'))
if sacar >= 50:
    print(f'Total de {sacar//50} cédulas de R$50')
    sacar %= 50
if sacar >= 20:
    print(f'Total de {sacar//20} cédulas de R$20')
    sacar %= 20
if sacar >= 10:
    print(f'Total de {sacar//10} cédulas de R$10')
    sacar %= 10
if sacar >= 1:
    print(f'Total de {sacar//1} cédulas de R$1')
    sacar %= 1
