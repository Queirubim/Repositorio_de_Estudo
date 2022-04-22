print('==========Conversor==========')
num = int(input('Digite um numero : '))
print('Escolha um numero para conversão')
print('>>1<<   BINÁRIO')
print('>>2<<   OCTAL')
print('>>3<<   HEXADECIMAL')
base = int(input('Sua ecolha foi : '))
if base == 1:
    ba = bin(num)
    b1 = 'Binario'
elif base == 2:
    ba = oct(num)
    b1 = 'Octal'
elif base == 3:
    ba = hex(num)
    b1 = 'Hexadecimal'
print(f'O numero, {num} convertido na base, {b1} é igual á, {ba[2:]} !')
