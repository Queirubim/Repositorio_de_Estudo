conti = conts = contmi = 0
sexo = fim = ' '
while True:
    print(f'''{'='*30}
{"CADASTRE UMA PESSOA": ^30}
{'='*30}''')
    idade = int(input('IDADE: '))
    while sexo not in 'MF':
        sexo = str(input('SEXO: [M/F] ')).upper().strip()[0]
    if idade > 18:
        conti += 1
    if sexo in 'M':
        conts += 1
    elif idade < 20:
        contmi += 1
    print('='*30)
    while fim not in 'SN':
        fim = str(input('Quer continuar ? [S/N] ')).upper().strip()[0]
    if fim == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos {conti}.
Ao todo temos {conts} homens cadatrados.
E temos {contmi} mulheres com menos de 20 anos.''')
