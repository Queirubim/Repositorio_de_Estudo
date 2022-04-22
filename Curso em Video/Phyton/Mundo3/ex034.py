def turma(*num, sit=False):
    lista = dict()
    n = 0
    for c in num:
        n += c
    lista['Total'] = len(num)
    lista['Maior'] = max(num)
    lista['Menor'] = min(num)
    lista['Media'] = n/lista['Total']

    if sit:
        if lista['Media'] > 6:
            lista['Situação'] = 'Boa'
        elif 4 <= lista['Media'] <= 6:
            lista['Situação'] = 'Media'
        else:
            lista['Situação'] = 'Ruim'
    return lista


resp = turma(3, 2, 2, 6.5, sit=True)
print(resp)
