# Створіть просту функцію favorite_movie, яка приймає рядок з назвою вашого улюбленого фільму.
# Потім функція має повернути рядок “My favorite movie is named {name}”.
# У кінці програми створіть змінну new_string зі своїм улюбленим фільмом
# (Наприклад, new_string = "2001: A Space Odyssey"), викличте новостворену функцію, передайте до неї new_string і
# виконайте print результату функції.
def favorite_movie(name):
    return "My favorite movie is named {}".format(name)


new_string = "2001: A Space Odyssey"

print(favorite_movie(new_string))