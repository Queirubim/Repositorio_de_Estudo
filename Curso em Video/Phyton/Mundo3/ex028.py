from time import sleep


def maior(* num):
    print('=='*24)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
        sleep(0.3)
    print(f'Foram imformados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
