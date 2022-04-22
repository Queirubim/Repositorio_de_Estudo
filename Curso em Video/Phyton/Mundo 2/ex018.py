frase = str(input('Digite uma frase: ')).upper().strip().split()
frase = ''.join(frase)
t = len(frase)
fi = str('')
for c in range(t - 1, -1, -1):
    fi += (frase[c])
print(f'O inverso de {frase} é {fi}. ')
if fi == frase:
    print('Temos um Palindromo:')
else:
    print('Essa frase não é um palindromo')
