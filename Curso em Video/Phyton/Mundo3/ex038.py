from uteis import moedas

p = float(input('Digite um Preçp: R$: '))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')
print(f'O dopro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10, True)}')
print(f'Reduxindo 13%, temos {moedas.diminuir(p, 13, True)}')
