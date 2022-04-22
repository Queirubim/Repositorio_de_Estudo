from moedas import adicionar, forma, menu, leiaInt
from time import sleep
while True:
    sleep(2)
    menu()
    op = leiaInt('\033[33mSua Opção:\033[m')
    if op > 3:
        print('\033[31mERRO Didite uma Opção Valida.\033[m')
    if op == 3:
        forma('SAINDO DO SISTEMA...')
        break
    if op == 2:
        adicionar()
    if op == 1:
        try:
            pessoas = open('texto.txt')
            forma('PESSOAS CADASTRADAS')
            for p in pessoas:
                print(f'{p[0:-4]}{" "*(36-len(p))}', end='')
                print(f'{p[-4:-1]:} anos')
        except:
            print('Não há Pessoas cadastradas!')
            print('Tente cadastrar alguma pessoa')
