# Створи програму, яка генерує рядок довжиною в 100 символів з випадкових цілих чисел від 0 до 9, і змінну input_str,
# яка буде посилатися на цей рядок.
import random
# your code goes here
input_str = ''
i = 1

while i <= 100:
    input_str = input_str + str(random.randint(1, 9))
    i += 1

print(input_str)   