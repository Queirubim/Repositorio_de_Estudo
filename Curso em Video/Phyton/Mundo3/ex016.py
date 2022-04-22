mat = list()
dados = list()
c = s = s2 = 0
while True:
    dados.append(int(input(f'Diga um valor para a posição [{len(mat)}, {c}]: ')))
    c += 1
    if c == 3:
        mat.append(dados[:])
        dados.clear()
        if len(mat) == 3 and c == 3:
            break
        c = 0

for v in mat:
    for p in v:
        if p % 2 == 0:
            s += p
        if p == v[2]:
            s2 += p
print('='*40)
for v, e in enumerate(mat):
    print(mat[v])
print('='*40)
print(f'A soma de todos os valores pares é {s}')
print(f'A soma dos valores da terceira cola é {s2}')
print(f'O maior valor da segunda linha é {max(mat[1])}.')
