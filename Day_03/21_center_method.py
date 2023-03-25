'''
Los métodos center( ), ljust( ) y rjust( ) alinean una cadena en el centro, la
izquierda o la derecha. Un segundo argumento indica con qué caracter se
deben llenar los espacios vacíos (por defecto un espacio en blanco).
'''

word = 'Hola mateo'
print(word.center(20, '*'))
print(word.ljust(20, '*'))
print(word.rjust(20, "&"))
