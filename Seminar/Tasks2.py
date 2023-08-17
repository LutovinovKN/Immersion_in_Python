# Создать класс прямоугольник
# Класс должен принимать длину и ширину при создании экземпляра
# у класса должно быть 2 метода, возвращающие периметр и площадь
# если при создании передаётся тоько одна сторона, считаем, что у нас квадрат

class rectangle:

    def __init__(self, len, width = None):
        self.len = len
        self.width = width
        if width is None:
            self.width = len

    def perimetr(self):
        return 2 * (self.len + self.width)

    def square(self):
        return self.len * self.width


res = rectangle(5)
print(res.square(), res.perimetr())

res2 = rectangle(5, 3)
print(res2.square(), res2.perimetr())
