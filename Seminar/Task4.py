# Создайте класс Моя Строка, где: будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)
from time import time, strftime, gmtime


class MyStr(str):
    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.value = value
        instance.name = name
        instance.init_time = strftime('%H:%M:%S', gmtime(time()))
        return instance

    def __str__(self):
        return str({'value': self} | self.__dict__)


my_line = MyStr("5", 'Vesper')

print(my_line)
