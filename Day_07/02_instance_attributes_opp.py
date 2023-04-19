class Bird:
    wings = 'Doradas'

    def __init__(self, color, kind):
        self.color = color
        self.kind = kind


my_bird = Bird('black', 'tucan')

print(
    f'Mi pajaro es un {my_bird.kind} y es de color {my_bird.color}'
)

print(Bird.wings)
print(my_bird.wings)
