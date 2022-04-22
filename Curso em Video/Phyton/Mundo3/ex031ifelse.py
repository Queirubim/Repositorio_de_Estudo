def fact(num, show=False):
    fa = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c} ', end='')
            print('x 'if c != 1 else '= ', end='')
        fa *= c
    return fa


print(fact(10, True))
