totg = maism = 0
maisb = menosp = ' '
while True:
    nome = str(input('NOME DO PRODUTO: '))
    preco = int(input('PREÇO: R$ '))
    if totg == 0:
        menosp = preco
        maisb = nome
    if preco < menosp:
        maisb = nome
    if preco > 1000:
        maism += 1
    totg += preco
    fim = ' '
    while fim not in 'NS':
        fim = str(input('Quer continuar ?[S/N]: ')).strip().upper()[0]
    if fim == 'N':
        break
print(f'''O total gasto foi {totg:.1f} R$
Existem {maism} produtos custando mais de 1000 R$
E o nome do produto mais barato é {maisb} que custa {menosp:.1f} R$''')
