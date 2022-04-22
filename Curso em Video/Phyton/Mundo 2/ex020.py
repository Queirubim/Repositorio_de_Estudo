maior = 0
menor = 100000
for c in range(1, 6):
    peso = int(input(f'Peso da {c}ª pessoa: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso lido foi {maior} e o menor foi {menor}')
