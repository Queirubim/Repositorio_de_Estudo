a = float(input('\033[0;31mLado 1 : '))
b = float(input('\033[0;32mlado 2 : '))
c = float(input('\033[0;34mlado 3 : \033[m'))
if a + b > c and a + c > b and c + b > a:
    print(f'Os lados: \033[1;32m{a,b,c}\033[m podem formar um triangulo')
else:
    print(f'Os lados: \033[1;32m{a,b,c}\033[m, não podem formar um triangulo')
