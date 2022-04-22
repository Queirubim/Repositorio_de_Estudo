while True:
    print('\033[42m='*28)
    print(f'  SISTEMA DE AJUDA PyHELP')
    print('=' * 28)
    fim = str(input('\033[mFunção ou biblioteca: '))
    if fim in 'fF':
        break
    print(f'\033[46m{"="*36}{"="*len(fim)}')
    print(f"Acessando o manual do comando '{fim}'")
    print(f'{"=" * 36}{"=" * len(fim)}')
    print(f'\033[m{help(fim)}')
