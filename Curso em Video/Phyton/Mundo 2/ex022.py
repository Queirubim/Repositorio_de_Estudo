sexo = str(input('Qual seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'sSmM':
        print('\033[31meErR0!!!\033[m')
        sexo = str(input('Qual seu sexo [F/M]: ')).strip().upper()[0]
print('Que bom que vc não foi idiota o bastante para não saber o que é sexo.')
