print(f'{"TABUADA":=^30}')
s = 0
tab = int(input('ESCOLHA UM NUMERO PARA TABUADA : '))
for c in range(0, 10):
    s += 1
    print(f'{tab} X {s} = {tab * s}')
