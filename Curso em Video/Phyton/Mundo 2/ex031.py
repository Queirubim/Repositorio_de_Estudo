s = c = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma de todos os {c} termos foi {s}.')
