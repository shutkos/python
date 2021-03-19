# Дано дві змінні: a_str і b_str, які мають певні рядкові значення. Напишіть програму, яка виконує print
# “a_str is bigger than b_str by N characters”, якщо довжина рядка a_str більше, ніж довжина b_str. .
# В іншому випадку, виконується print “b_str is bigger than a_str by N characters”.
# N – це різниця кількості символів у двох рядках. Якщо рядки однакової
# довжини, print “a_str and b_str lengths are equal”.
a_str = "1D+3qwKBgESv4cYluNDRLl7aACr"
b_str = "Jq77sGRFnnHkTmcQLfZKJdOJEmRALYS8tLoZM"
# your code goes here
if a_str > b_str:
    n = len(a_str) - len(b_str)
    print("a_str is bigger than b_str by {0} characters".format(n))
elif a_str < b_str:
    n = len(b_str) - len(a_str)
    print('b_str is bigger than a_str by {0} characters'.format(n))
else:
    print("a_str and b_str lengths are equal")