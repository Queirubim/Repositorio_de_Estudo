print(f'{"LOJA SINCERA":=^40}')
pagar = float(input('Qual o valor da sua compra :'))
itens = ('DINHEIRO', 'DEBITO', '2X', '3X')
print('''Agora escolha a forma de pagamento
>>0<<   DINHEIRO
>>1<<   DEBITO
>>2<<   DIVIDIDO 2X
>>3<<   DIVIDIDO 3X Ou + ''')
fp = int(input('Opção: '))
if fp == 0:
    preco = pagar - (10 * pagar) / 100
elif fp == 1:
    preco = pagar - (5 * pagar) / 100
elif fp == 2:
    preco = pagar
else:
    div = int(input('Em quantas vezes deseja dividir : '))
    preco = pagar + (20 * pagar) / 100
    print(f'Voce pagara {div} parcelas de R$:{preco/div}')
print(f'A forma de pagamento escolhida foi {itens[fp]} conta ficou R$:{preco}.')
