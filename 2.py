#2
class Figure(ABC):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @abstractmethod
    def calculateArea():
        pass


class Triangle(Figure):
    def calculateArea(self):
        return 0, 5 * self.width


class Rectangle(Figure):
    def calculateArea(self):
        return self.height * self.width * self.height


figures = [Rectangle(10, 5), Triangle(10, 5)]

for figure in figures:
    print(figure.calculateArea())
