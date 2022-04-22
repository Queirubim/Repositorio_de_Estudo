from datetime import date
cont0 = 0
cont1 = 0
for c in range(0, 7):
    dn = int(input('Digite o ano que vc nasceu: '))
    idade = date.today().year - dn
    if idade >= 21:
        cont0 += 1
    else:
        cont1 += 1
print(f'Das 7 pessoas intrevistadas \033[32m{cont0}\033[m atingiram a maior idade e \033[31m{cont1}\033[m ainda não atingiram')
