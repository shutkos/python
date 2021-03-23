# Дана змінна a_str зі значенням 'OBD8XZYF1F96KRI207H17K0PJF6M2W5C' і b_str зі значенням
# 'RJUAKY9QKJVJIDWFZQPJ8293EEEO9SB8ZH832HTOP'. Напишіть програму, яка підрахує суму абсолютних різниць
# Unicode-кодів символів з однаковими позиціями в обох рядках. Зверніть увагу, що наведені рядки неоднакової довжини.
# Вам потрібно створити один цикл while для ітерації над обома рядками, і відсутні символи повинні бути замінені на
# значення 0. Запишіть результат обчислень в змінну на ім’я res.
a_str = 'OBD8XZYF1F96KRI207H17K0PJF6M2W5C'
b_str = 'RJUAKY9QKJVJIDWFZQPJ8293EEEO9SB8ZH832HTOP'

res = 0
i = 0

while True:
    if len(a_str) <= i:
        res += abs(0 + ord(b_str[i]))
    else:
        res += abs(ord(a_str[i]) - ord(b_str[i]))
    i = i + 1
    if i >= len(b_str):
        break

print(res)