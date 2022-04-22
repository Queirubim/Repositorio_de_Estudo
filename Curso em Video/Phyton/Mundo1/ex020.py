num = int(input('Digite um numero : '))
#print(f'unidade : {num[3]}')
#print(f'desena : {num[2]}')
#print(f'centena : {num[1]}')
#print(f'milhar : {num[0]}')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Desena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
