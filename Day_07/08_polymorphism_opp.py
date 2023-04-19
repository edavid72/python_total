class Cow:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} say muuu')


class Goat():

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} say beee')


cow1 = Cow('Aurora')
goat1 = Goat('Tobias')

lista = [cow1, goat1]

for animal in lista:
    animal.talk()

def animal_talk(animal):
    animal.talk()

animal_talk(cow1)