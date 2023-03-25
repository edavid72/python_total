'''
isprintable( ): determina si todos los caracteres de la cadena son
imprimibles (es decir, no son caracteres especiales indicados por \...).
'''

word ='this is a test'
print(word.isprintable())

word2 = 'this is a\ntest'
print(word2.isprintable())