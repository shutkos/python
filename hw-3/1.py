# Напишіть Python-програму для виведення найбільшого числа зі списку випадкових чисел довжиною в 10 елементів.
# Обмеження: використовуйте тільки цикл while і модуль random для генерації чисел.
import random
random_list = []
counter = 1

while counter <= 10:
    random_list.append(random.random())
    counter = counter + 1

print(max(random_list))