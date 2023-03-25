from random import shuffle


def lanzar_dados():
    valores = [1, 2, 3, 4, 5, 6]
    shuffle(valores)
    return valores[0:2]


func_lanzar_dados = lanzar_dados()


def evaluar_jugada(num1, num2):
    mensaje = ''
    suma_dados = num1 + num2
    if suma_dados <= 6:
        mensaje = f'La suma de tus dados es {suma_dados}. Lamentable'
    elif suma_dados > 6 and suma_dados < 10:
        mensaje = f'La suma de tus dados es {suma_dados}. Tienes buenas chances'
    elif suma_dados >= 10:
        mensaje = f'La suma de tus dados es {suma_dados}. Parece una jugada ganadora'

    return mensaje


print(evaluar_jugada(func_lanzar_dados[0], func_lanzar_dados[1]))
