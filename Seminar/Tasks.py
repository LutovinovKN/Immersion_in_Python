# Создайте класс окружность
# Класс должен принимать радиус окружности при создании экземпляра
# У класс должно быть 2 метода, возвращающие длину окружности и её площадь
import math


class Round:
    def __init__(self, radius):
        self.radius = radius

    def len_round(self):
        return 2 * math.pi * self.radius


    def square_round(self):
        return math.pi * self.radius ** 2

    @classmethod
    def square_to_circ(cls, square_round):
        return cls((square_round / math.pi) ** 0.5)


rad = int(input('Введите радиус окружности:'))
p1 = Round(rad)
p2 = Round.square_to_circ(rad)


print(p1.len_round(), p1.square_round())
print(p2.radius)
