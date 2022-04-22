import requests
try:
    res = requests.get('http://pudim.com.br/')
    if res.status_code == 200:
        print('\033[32mO site esta funcionando !\033[m')
except:
    print('\033[31mO site não esta funcionando !\033m')
