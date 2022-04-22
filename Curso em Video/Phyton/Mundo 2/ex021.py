im = 0
idh = 0
nh = ''
mu = 0
for c in range(1, 5):
    print(f'======={c}ª PESSOA=======')
    sexo = str(input('Qual seu sexo [M/F]: ')).upper()
    nome = str(input('Qual sua nome: '))
    idade = int(input('Qual sua idade: '))
    im += idade
    if sexo == 'M' and idade > idh:
        idh = idade
        nh = nome
    elif sexo == 'F' and idade <20:
       mu += 1
print(f'A idade media do grupo é {im/4}.')
print(f'O homenm mais velho tem {idh} anos e se chama {nh}.')
print(f'Existem {mu} mulheres abaixo de 20 anos.')
