lis = []
expressao = str(input('Digite um expressão matematica qualquer com parênteses: '))
for el in expressao:
    if el == '(':
        lis.append('(')
    elif el == ')':
        if len(lis) > 0:
            lis.pop()
        else:
            lis.append(')')
            break #nesse momento ele viu que o 1 parenteses era aberto e logo toda expressão estava errada
print(f'{len(lis)} {lis}')
if len(lis) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
