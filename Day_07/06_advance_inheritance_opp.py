class Animal:

    def __init__(self, age, color):
        self.age = age
        self.color = color

    def born(self):
        print('this animal was born')

    def talk(self):
        print('this animal makes a sound')


class Bird(Animal):

    # attributes
    def __init__(self, age, color, flight_height):
        super().__init__(age, color)
        self.flight_height = flight_height

    def talk(self):
        print('pio pio')

    def fly(self, meters):
        print(f'this animal fly {meters} meters')

    def altura_vuelo(self):
        print(f'este animal esta volando a')




piolin = Bird(4, 'amarillo', 44)

piolin.talk()
piolin.fly(23)

my_animal = Animal(33,'rojo')

my_animal.color
