'''
isdigit( ): determina si todos los caracteres de la cadena son dígitos, o
pueden formar números, incluidos aquellos correspondientes a lenguas
orientales.
'''

digits = '123456'
print(digits.isdigit())

digits2 = '23+33'
print(digits2.isdigit())

digits3 = '1222m338798'
print(digits3.isdigit())