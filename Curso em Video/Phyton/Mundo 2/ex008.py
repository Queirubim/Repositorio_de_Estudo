peso = float(input('Qual seu em kg : '))
altura = float(input('Qual sua altura em Metros : '))
imc = peso / (altura ** 2)
if imc < 18.5:
    p = str('MAGRESA')
elif imc < 25:
    p = str('NORMAL')
elif imc < 30:
    p = str('SOBREPESO')
elif imc < 40:
    p = str('OBESIDADE')
else:
    p = str('\033[31mVAI SE TRATAR PORRA')
print(f'Seu IMC: \033[97m{imc:.1f}\033[m')
print(f'Voce esta na faixetaria : {p}.')
