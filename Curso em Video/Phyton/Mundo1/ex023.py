frase = input('Digite uma frase :')
frase1 = frase.lower().strip()
print('A letra ,a, aprere ', frase.count('a'), ' vezes !')
print('A primeira letra a se encontra na casa ', frase1.find('a'))
print('E a ultima letra a se encontra na casa ', frase1.rfind('a'))
