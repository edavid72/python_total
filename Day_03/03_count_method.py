'''
1. count( ) : retorna el número de veces que se repite un conjunto de
caracteres especificado.
'''

phrase = 'Nunca dejes que nadie te diga que no puedes hacer algo. Ni siquiera yo. Si tienes un sueño, tienes que protegerlo. Las personas que no son capaces de hacer algo por ellos mismos, te dirán que tú tampoco puedes hacerlo. ¿Quieres algo? Ve por ello y punto'

word = 'algo'

print(f"The word 'hecer' is repeated {phrase.count('hacer')} times.")
print(f"The word '{word}' is repeated {phrase.count(word)} times.")

