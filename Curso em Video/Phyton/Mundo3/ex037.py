from uteis.moedas import moeda, metade, dobro, aumentar, diminuir

p = float(input('Digite um Preçp: R$: '))
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O dopro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10%, temos {moeda(aumentar(p, 10))}')
print(f'Reduxindo 13%, temos {moeda(diminuir(p, 13))}')
