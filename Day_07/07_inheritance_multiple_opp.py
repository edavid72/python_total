class Father:
    def talk(self):
        print('Hola')

class Mother:
    def smile(self):
        print('jajaj')


class Son(Father, Mother):

    def corregir(self):
        print('ponte a estuadias')

class Grandson(Son):
    pass



my_grandson = Grandson()


my_grandson.talk()
my_grandson.smile()
my_grandson.corregir()
