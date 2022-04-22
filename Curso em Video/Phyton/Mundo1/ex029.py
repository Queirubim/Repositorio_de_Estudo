#from datetime import date
print('Lhe direi se o ano é Bissexto !')
print('Se quiser saber o ano atual digite 0 ')
ano = int(input('Diga um ano : '))
#if ano == 0
    #ano = date.today().year
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('O ano é Bissexto')
        else:
            print('O ano não é Bissexto')
    else:
        print('O ano é Bissexto')
else:
    print('O ano não é Bissexto')
#if ano % 4 == 0 and % 100 != 0 or % 400 == 0:
