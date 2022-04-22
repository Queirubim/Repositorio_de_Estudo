mat = list()
dados = list()
c = 0
while True:
    dados.append(int(input(f'Diga um valor para a posição [{len(mat)}, {c}]: ')))
    c += 1
    if c == 3:
        mat.append(dados[:])
        dados.clear()
        if len(mat) == 3 and c == 3:
            break
        c = 0
print('='*40)
for v, e in enumerate(mat):
    print(mat[v])
