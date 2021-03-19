# Дана змінна a_str зі значенням 'OBD8XZYF1F96KRI207H17K0PJF6M2W5C'. Напишіть програму, яка обраховує суму коду
# Unicode всіх символів в цьому рядку.
a_str = "OBD8XZYF1F96KRI207H17K0PJF6M2W5C"

res = 0
counter = 0

while counter < len(a_str):
    res = res + ord(a_str[counter])
    counter = counter + 1

print(res)
