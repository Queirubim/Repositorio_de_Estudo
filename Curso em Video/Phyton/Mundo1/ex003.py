a = input('Digite Algo: ')
print('O tipo primitivo disso é {}!'.format(type(a)))
print('Só tem espaços ?', a.isspace())
print('É um numero ?', a.isnumeric())
print('É alfabetico ?', a.isalpha())
print('É alfanumérico ?', a.isalnum())
print('Esta em maiusculo ?', a.isupper())
print('Esta em minusculo ?', a.islower())
print('Esta capitalizada ?', a.istitle())
