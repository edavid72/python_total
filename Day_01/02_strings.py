'''
Los strings en Python son un tipo de dato formado por
cadenas (o secuencias) de caracteres de cualquier tipo,
formando un texto.

concatenación
Unificación de cadenas de texto:
print("Hola" + " " + "mundo")
>> Hola mundo

caracteres especiales
Indicamos a la consola que el caracter a continuación del
símbolo \ debe ser tratado como un caracter especial.
\" > Imprime comillas
\n > Separa texto en una nueva linea
\t > Imprime un tabulador
\\ > Imprime la barra invertida textualmente
'''

# simple string
print('hola mundo')

# concatenation
print('hello' + ' ' + 'mateo' + ' ' + 'how are you?')

# special characteres
print("Hello my name is \"David\"")
print('This is a line\nAnd this is a other line\nAnd other line')
print('1\t2\t3')
print('This isn\'t a number')
print('This \\ is a inverted bar')