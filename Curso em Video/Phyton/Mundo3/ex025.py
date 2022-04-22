def area(a, b):
    s = a * b
    print(f'A área de um terreno {a}x{b} é de {s}m².')


print(' Controle de terrenos')
print('='*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
