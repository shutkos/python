# Створіть список з усіма цілими числами від 1 до 100, потім знайдіть всі, які діляться на 7, але не діляться на 5, і
# розмістіть їх в окремому списку. Виведіть цей список у stdout із використанням функції print.
# Обмеження: використовуйте тільки цикл while для ітерацій.
first_list = range(100)
std_out = []
counter = 0

while counter < 100:
    # first_list.append(counter)

    if first_list[counter] % 7 == 0 and first_list[counter] % 5 != 0:
        std_out.append(first_list[counter])

    counter = counter + 1

print(std_out)