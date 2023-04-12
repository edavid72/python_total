from pathlib import Path

carpeta = Path(
    '/home/dcervellon/Documents/Programming/New-Stack2023/Python/Python-Total/Day_06/testa.txt')

# print(carpeta.name)
# print(carpeta.read_text())
# print(carpeta.exists())

if carpeta.exists():
    print('Si existo')
else:
    print('no estoy')
