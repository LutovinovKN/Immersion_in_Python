# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.
import fractions


# f1=fractions.Fraction(5, 2)
# f2=fractions.Fraction(2, 5)
# print(f1+f2, " & ", f1*f2)
# f3=fractions.Fraction(100, 10)
# print(f3)
fract1 = [int(x) for x in (input("Введите дробь типа (a/b): ").split("/"))]
fract2 = [int(x) for x in (input("Введите вторую дробь типа (a/b): ").split("/"))]

print(fract1, fract2)

tmp1 = fract1[0]*fract2[1] + fract2[0]*fract1[1]
tmp2 = fract1[1]*fract2[1]
summ = tmp1 / tmp2

print(summ)

mult = (fract1[0] * fract2[0]) / (fract1[1] * fract2[1])

print(mult)
