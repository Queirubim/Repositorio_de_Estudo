viagem = int(input('Qual distancia Voçê percorreu nessa viagem : '))
if viagem <= 200:
    taxa = 0.50
else:
    taxa = 0.45
print(f'o valor da sua taxa foi R$:{taxa} e o lavor que voçê vai pagar é R$:{viagem * taxa:.2f}')
