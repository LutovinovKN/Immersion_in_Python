# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку. При нового экземпляра класса,
# старые данные из ранее созданных экземпляров сохраняются в
# пару списков-архивов list-архивы также являются свойствами экземпляра

class Archive:
    _instance = None

    def __new__(cls, num, string):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.arh_num = []
            cls._instance.arh_str = []
        cls._instance.arh_num.append(num)
        cls._instance.arh_str.append(string)
        return cls._instance

    def __int__(self, num, string):
        self.num = num
        self.string = string

    def __str__(self):
        return f'{self.num}, {self.string}, {self.arch_num}, {self.arh_str}'
