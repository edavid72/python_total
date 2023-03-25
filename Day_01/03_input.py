''''
Función que permite al usuario introducir información por
medio del teclado al ejecutarse, otorgándole una instrucción
acerca del ingreso solicitado. El código continuará
ejecutándose luego de que el usuario realice la acción.
input("Dime tu nombre: ")
>> Dime tu nombre: |
Ingreso por teclado
print("Tu nombre es " + input("Dime tu
nombre: "))
>> Dime tu nombre: Federico
>> Tu nombre es Federico
'''

# Input
name = input('What is your name: ')
last_name = input('What is yor last name: ')

print(f'Hola {name} {last_name}')