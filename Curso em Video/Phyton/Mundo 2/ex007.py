a = float(input('\033[0;31mLado 1 : '))
b = float(input('\033[0;32mlado 2 : '))
c = float(input('\033[0;34mlado 3 : \033[m'))
if a + b > c and a + c > b and c + b > a:
    print(f'Os lados: \033[1;32m{a, b, c}\033[m podem formar um triangulo')
    # if a == b == c:
    if a == b and b == c:
        print('O Triangulo é Equilatero.')
        print('Ou seja, com todos os lados iguais.')
    elif a == b or b == c or c == a:
        print('O Triangulo é Isosceles.')
        print('Ou seja, com dois lados iguais.')
    else:
        print('O Triangulo é Escaleno.')
        print('Ou seja, todos os lados diferentes.')
else:
    print(f'Os lados: \033[1;32m{a, b, c}\033[m, não podem formar um triangulo')
