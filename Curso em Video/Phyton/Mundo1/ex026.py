vel = int(input('Qaul a Velocidade Do Carro: '))
if vel >= 80:
    print('Voçê foi multado !')
    print(f'O valor da sua multa foi R$:{7 * (vel - 80)}')
else:
    print('Voçê não foi multado !')
