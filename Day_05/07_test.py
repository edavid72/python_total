from random import choice


def lanzar_moneda():
    opcion = ['Cara', 'Cruz']

    resultado = choice(opcion)
    print(resultado)
    return resultado



resultado_p_func = lanzar_moneda()

lista_numeros = [1, 5, 4, 2, 6, 87, 8, 6]


def probar_suerte(resultado, lista):
    if resultado == 'Cara':
        print("La lista se autodestruirá")
        lista.clear()
        print(lista)

    else:
        print("La lista fue salvada")
        print(lista)
        return lista


probar_suerte(resultado_p_func, lista_numeros)
