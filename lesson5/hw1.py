# импортирую модуль рандома
import random
# 1. инициализируем переменную типа лист
mylist = []
# пока длинна листа меньше 10
while len(mylist)<10:
    # добавить в лист рандомное число
    mylist.append(random.randint(1,100))

# в переменную max_val берем первый элемент из листа.
max_val = mylist[0]
# обьявляем переменную счетчик
i = 0
# в цикле пока счетчик меньше чем длинна листа
while i < len(mylist):
    # если і-ый элемент больше записанного в переменной
    if max_val < mylist[i]:
        # записать в переменнує і-ый элемент
        max_val = mylist[i]
    # увеличить счетчик на 1
    i += 1

# вывести лист в котором искали и максимальное найденное число.
print(f"В листе {mylist}\nмаксимальное число {max_val}")