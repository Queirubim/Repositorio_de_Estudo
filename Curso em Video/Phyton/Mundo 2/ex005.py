n1 = float(input('Nota do semestre 1: '))
n2 = float(input('Nota do semestre 2: '))
m = (n1 + n2) / 2
if m < 5:
    r = str('\033[31mREPROVADO\033[m')
elif m >= 7:
    r = str('\033[32mAPROVADO\033[m')
else:
    r = str('\033[33mRECUPERAÇÃO\033[m')
print(f'Sua media foi {m:.2f} voce foi {r}!!!')
