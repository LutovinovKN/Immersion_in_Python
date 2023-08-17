#Решить задачи, которые не успели решить на семинаре.
table = 'ТАБИЦА УМНОЖЕНИЯ'
print(table.center(40))
for num in range(1, 10, 3):
    for count in range(1, 11):     
        print(num, 'x', count, '=', num * count, '\t',
              (num1 := num + 1), 'x', count, '=', num1 * count, '\t',
              (num2 := num + 2), 'x', count, '=', num * count)
    print("\n")