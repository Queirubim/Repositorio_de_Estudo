from random import shuffle
a4 = str(input('Aluno 1:'))
a3 = str(input('aluno 2:'))
a2 = str(input('aluno 3:'))
a1 = str(input('aluno 4:'))
li = [a1, a2, a3, a4]
shuffle(li)
print(f'A ordem de apresentação sera {li} !')
