#Программа загадывает число от 0 до 1000. 
#Необходимо угадать число за 10 попыток. 
#Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# 
# Для генерации случайного числа используйте код:
import emoji
from random import randint
num = randint(0, 1001)


n = 0
while n < 11:
    attempt = int(input())
    if attempt == num:
        print(emoji.emojize('Вы угадали! :thumbs_up:'))
        break
    elif attempt < num:
        print(emoji.emojize('Бери число больше :backhand_index_pointing_up:'))
    else: print(emoji.emojize("Бери число меньше :backhand_index_pointing_down:"))
    n += 1
print(num)