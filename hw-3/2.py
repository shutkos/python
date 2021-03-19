# Згенеруйте два списки first_list і second_list, довжиною в 10 елементів, які містять випадкові цілі числа
# від 1 до 10, потім створіть третій список з усіх спільних цілих чисел у першому та другому списках, але
# без повторень, і виведіть цей список у stdout із використанням функції print.
# Обмеження: використовуйте тільки цикл while і модуль random для генерації чисел.
# write your program here
import random

first_list = []
second_list = []
counter = 1

while counter <= 10:
    first_list.append(random.randint(1, 10))
    second_list.append(random.randint(1, 10))
    counter = counter + 1

std_out = list(set(first_list) & set(second_list))

print(std_out)