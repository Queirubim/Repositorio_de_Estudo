from datetime import date
nas = int(input('Em que ano voce nasceu : '))
idade = date.today().year - nas
if idade <= 9:
    clas = str('MIRIM')
elif idade <= 14:
    clas = str('INFALTIL')
elif idade <= 19:
    clas = str('JUNIOR')
elif idade <= 20:
    clas = str('SENIOR')
else:
    clas = str('MASTER')
print(f'Com {idade} anos voce se clasifica na colocação:\033[34m{clas}\033[m.')
