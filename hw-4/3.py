# Створіть функцію make_operation, яка приймає першим параметром простий арифметичний оператор (для спрощення нехай
# це буде ‘+’, ‘-’ і ‘*’) у вигляді рядка та випадкову кількість аргументів (тільки цілі числа або числа з рухомою
# комою) другим параметром. Потім функція має повернути результат додавання, віднімання та множення всіх чисел в
# другому параметрі.
# Наприклад:
# виклик make_operation(‘+’, 7, 7, 2) повинен повернути 16
# виклик make_operation(‘-’, 5, 5, -10, -20) повинен повернути 30
# виклик make_operation(‘*’, 7, 6) повинен повернути 42
# Також треба додати валідацію введених параметрів і викликати відповідні помилки, якщо їхній тип неправильний.
def make_operation(operator, *args):
    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        raise ValueError
    else:
        if operator == '+':
            summa = 0
            for arg in args:
                summa = summa + arg
            return summa
        elif operator == '-':
            summa = args[0]
            for arg in args[1:len(args)]:
                summa = summa - arg
            return summa
        elif operator == '*':
            summa = 1
            for arg in args:
                summa = summa * arg
            return summa
        elif operator == '/':
            summa = 1
            for arg in args:
                summa = summa / arg
            return summa
        else:
            return None