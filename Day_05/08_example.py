precios_cafe = [('capuchino', 1.5), ('expreso', 2.2), ('moka', 1.9)]


def cafe_mas_caro(precios_cafe):
    precio_mayor = 0
    mafe_mas_caro = ''

    for cafe, precio in precios_cafe:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass

    return (precio_mayor, cafe_mas_caro)


print(cafe_mas_caro(precios_cafe))
