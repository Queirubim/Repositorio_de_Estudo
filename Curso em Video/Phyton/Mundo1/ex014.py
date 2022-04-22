from math import hypot, pow
ca = float(input('Qual o cumprimento do cateto adjacente :'))
co = float(input('Qaul o cumprimento do cateto oposto :'))
hi = hypot(ca, co)
print(f'A hipotenusa do seu triangulo é {hi:.2f}')
po = pow(ca, co)
print(po)
