#Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
#Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
from sympy import *


def check_input():
    while True:
        num = input("Введите число: ")
        if num.isdecimal() and 0 < (res := int(num)) < 100000:
            return res
        print("введите число от 0 до 100 тыс.")


n = check_input()
flag1 = isprime(n)
if flag1 == True:
    print("Вариант 1 решения: Это простое число")
else: print("Вариант 1 решения: Это составное число")

print("""
    ---Решение №2---
    """)

p = check_input()
flag = True

for i in range(2, p):
    if p % i == 0:
        flag = False
if p > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')