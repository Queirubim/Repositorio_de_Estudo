from datetime import date
print('=======ALISTAMENTO=======')
nas = int(input('Qual Sua data de nascimento : '))
ida = date.today().year - nas
print(f'Quem nasce em {nas}, tem {ida} anos em {date.today().year}.')
if ida < 18:
    print(f'Ainda faltam {18 - ida} anos para vc se alistar')
    verbo = str('será')
elif ida == 18:
    print(f'Com {ida} anos ja esta na hora de voce se alistar.')
    verbo = str('é')
else:
    print(f'Voce ja deveria ter se alistado a {ida - 18} anos.')
    verbo = str('foi')
print(f'Seu alistamento {verbo} em {nas + 18}.')
