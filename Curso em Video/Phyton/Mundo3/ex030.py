def voto():
    from datetime import date
    idade = date.today().year - nas
    if idade < 18:
        c = 'Nâo pode Votar'
    elif 65 >= idade >= 18:
        c = 'O voto é Obrigatorio'
    elif idade >= 65:
        c = 'O voto é Facutativo'
    print(f'Com {idade} anos: {c}')


print('='*30)
nas = int(input('Em que ano voçê nasceu ?: '))
voto()
