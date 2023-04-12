import os

change_dir = os.chdir(
    '/home/dcervellon/Documents/Programming/New-Stack2023/Python/Python-Total/Day_06/alternative')

actual_dir = os.getcwd()

my_file = open('prueba.txt')

print(my_file.read())

# new_dir = os.makedirs('/home/dcervellon/Documents/Programming/New-Stack2023/Python/Python-Total/Day_06/alter')

ruta = '/home/dcervellon/Documents/Programming/New-Stack2023/Python/Python-Total/Day_06'

element = os.path.basename('/home/dcervellon/Documents/Programming/New-Stack2023/Python/Python'
                           '-Total/Day_06/test.txt')

dirname = os.path.dirname(ruta)

print(element)

print(dirname)

remove_dir = os.rmdir('/home/dcervellon/Documents/Programming/New-Stack2023/Python/Python'
                      '-Total/Day_06/alter')

print(os.getcwd())