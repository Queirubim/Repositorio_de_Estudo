print('Diga 3 numeros distintos de 0 a 9:')
n1 = int(input('n1 : '))
n2 = int(input('n2 : '))
n3 = int(input('n3 : '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print(f'O maior numero é: {maior}')
print(f'O menor numero é: {menor}')
