class Bird:
    wings = True

    def __init__(self, color, kind):
        self.color = color
        self.kind = kind

    def piar(self):
        print('pio')

    def fly(self, meters):
        print(f'El parajaro volo {meters} metros')
        self.piar()

    def paint_black(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    @classmethod
    def lay_eggs(cls, qty):
        print(f'Puso {qty} huevos')
        cls.wings = 'Si vuela'
        print(Bird.wings)

    @staticmethod
    def see():
        print('eso mira')


piolin = Bird('amarillo', 'tucan')

piolin.paint_black()

piolin.fly(12)


Bird.lay_eggs(23)


Bird.see()