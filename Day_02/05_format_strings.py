'''

Función format: se encierra las posiciones de las variables
entre corchetes { }, y a continuación del string llamamos a
las variables con la función format
print("Mi auto es {} y de matrícula
{}".format(color_auto,matricula))

Cadenas literales (f-strings): a partir de Python 3.8,
podemos anticipar la concatenación de variables
anteponiendo f al string
print(f"Mi auto es {color_auto} y de
matrícula {matricula}")

'''

# Format function

color_car = 'red'
matriculate = 76767

print('My car is color {} and your matriculate is {}'.format(color_car, matriculate))

# Literal strings
color_book = 'blue'
price = 100

print(f'That book is color {color_book} and your price is {price}')
