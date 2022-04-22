from uteis import moedas

p = float(input('Digite um Preçp: R$: '))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dopro de {p} é {moedas.dobro(p)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10)}')
print(f'Reduxindo 13%, temos {moedas.diminuir(p, 13)}')
