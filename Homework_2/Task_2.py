# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата. 

def convert(basis: int, number: int):
    res = []
    #string = ""
    while number > 0:
        digit = str(number % basis)
        number //= basis

        res.append(digit)
        # print(res)
        
        #return res
    return "".join(res[::-1])

x = convert(int(input("Введите в какую систему счисления перевести число:")), int(input("Введите число:")))
print(x)
