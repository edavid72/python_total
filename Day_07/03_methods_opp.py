class Bird:
    wings = True

    def __init__(self, color, kind):
        self.color = color
        self.kind = kind

    # Methods
    def piar(self):
        print(f'pio, hola me llamo piolin y soy una {self.kind} de color {self.color}')

    def fly(self, meters):
        print(f'El pajaro volo {meters} metros')


piolin = Bird('amarillo', 'caricatura')


piolin.fly(12)
piolin.piar()