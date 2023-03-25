'''
find( ) e index( ) retornan la ubicación (comenzando desde el cero) en la
que se encuentra el argumento indicado. Difieren en que index lanza
ValueError cuando el argumento no es encontrado, mientras find retorna
-1.
'''

phrase = 'Nunca dejes que nadie te diga que no puedes hacer algo. Ni siquiera yo. Si tienes un sueño, tienes que protegerlo. Las personas que no son capaces de hacer algo por ellos mismos, te dirán que tú tampoco puedes hacerlo. ¿Quieres algo? Ve por ello y punto'

# find method
print('find method')
find_phrase = phrase.find('personas')
print(find_phrase)

find_not_phrase = phrase.find('nuclear')
print(find_not_phrase)
print('\n')

# index method
print('index method')
index_phrase = phrase.index('personas')
print(index_phrase)
index_not_phrase = phrase.index('nuclear')