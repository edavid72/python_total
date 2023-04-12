from pathlib import Path

directory = Path('/home/dcervellon/Documents/Programming/New-Stack2023/Python/Python-Total/Day_06')

file = directory / 'test.txt'

my_file = open(file)

print(my_file.read())
