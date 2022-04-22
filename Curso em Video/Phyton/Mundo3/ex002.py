lol = ('paiN Gaming', 'INTZ', 'KaBuM', 'Prodigy', 'Santos HotForex', 'Flamengo', 'FURIA', 'Keyd', 'Redemption', 'Patolicos')
print(f'''Os 5 primeiros colocados são: 
{lol[:5]}
Os quatro ultimos colocados são:
{lol[-4:]}
A lista em ordem alfabetica fica:
{sorted(lol)}
A keyd esta na {lol.index('Keyd')+1}ª posição.''')
