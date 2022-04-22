n = nd = ns = 0
print('Va digitando diversos numeros inteiros')
print('Dica, se quiser parar bastar o nome da gravadora de Baco')
while n != 999:
    n = int(input('=> '))
    if n != 999:
        nd += 1
        ns += n
print(f'A soma dos {nd} termos foi {ns}.')
