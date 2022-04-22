acumulador = 0
somador = 0
for c in range(0, 6):
    num = int(input('Diga um numero : '))
    if num % 2 == 0:
        acumulador += num
        somador += 1
print(f'A somo de todos os {somador} numeros pares foi {acumulador}')
