class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        selfcolor = color
    def draw(self):
        return 'Рисуем фигуру'


class Line(Figure):
    def draw(self):
        return 'рисцем линию'

class React(Figure):

    def __init__(self,  coords, width, color, side):
        super().__init__( coords, width, color)
        self.side=side

    def draw(self):
        return 'прямоугольник'

    def square(self):
        return self.side**2


class Ellipse(Figure):
    def draw(self):
        return 'элипс'


def try_to_draw(obj):
    print(obj.draw())


f = Figure([1, 2, 3, 4, 5, 6], 3, 'black')

# print(f.coords)
# print(f.draw())
L = Line([1, 1, 5, 5], 2, 'red')
# print(f'{L.draw()}толщиной {L.draw()} и цветом {L.color}')
r = React([1,1, 6,6], 5, 'yellow', 4)
try_to_draw(f)