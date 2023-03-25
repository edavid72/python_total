'''
replace( ) reemplaza una cadena por otra.
'''

word = 'hola mateo como estas'
print(word)
word_replace = word.replace('mateo', 'mateoooo')
print(word_replace.replace('mateoooo', 'david'))

frase = 'Si la implementación es difícil de explicar, puede que sea una mala idea'
frase = frase.replace('difícil', 'fácil')
frase = frase.replace('mala', 'buena')
print(frase)
