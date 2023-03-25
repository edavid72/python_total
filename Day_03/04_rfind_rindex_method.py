'''
rfind( ) y rindex( ).Para buscar un conjunto de caracteres pero desde el
final.
'''
phrase = 'Nunca dejes que nadie te diga que no puedes hacer algo. Ni siquiera yo. Si tienes un sueño, tienes que protegerlo. Las personas que no son capaces de hacer algo por ellos mismos, te dirán que tú tampoco puedes hacerlo. ¿Quieres algo? Ve por ello y punto'


print('startswith method')
starswith_method = phrase.startswith('Nunca')
print(starswith_method)
print('\n')

print('endswith method')
endswith_method = phrase.endswith('punto')
print(endswith_method)
