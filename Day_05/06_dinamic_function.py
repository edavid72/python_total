def chequear_3_cifras(lista):
    list_3 = []

    for n in lista:
        if n in range(100, 1000):
            list_3.append(n)
        else:
            pass

    return  list_3

print(chequear_3_cifras([12,55,6,53,222,2222,992]))
