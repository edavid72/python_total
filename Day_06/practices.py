def sobrescribir(file):
    open_file = open(file, 'w')
    write_file = open_file.write('contenido eliminado')

    open_file.close()
    return write_file



