val = list()
for c in range(1, 6):
    num = int(input('Digite um numero: '))
    if c == 1 or num > val[len(val)-1]:#o ultimo e maior valor da lista
        val.append(num)
        print('O numero foi adicionado ao final da lista...')
    else:
        for d in val:
            if d > num:
                val.insert(val.index(d), num)
                print(f'Adicionado na posição {val.index(num)} da lista...')
                break
print('-'*45)
print(f'Os valores digitados em ordem foram {val}')
