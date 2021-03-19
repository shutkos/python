# Напишіть код create_file, який створює новий файл виводу під назвою myfile.txt і запишіть в нього рядок
# "Hello file world!". Потім напишіть код read_file, який відкриває myfile.txt і повертає його вміст у вигляді рядка.
# В кінці свого рішення не забудьте викликати read_file передавши до неї назву нашого файлу та виведіть результат
# виконання функції за допомогою функції print.
# Примітка: методи написання файлів не додають символи нового рядка, потрібно додавати ‘\n’ у кінці рядка,
# якщо хочете перервати рядок у файлі.
def create_file(file_name):
    f = open(file_name, 'w')
    f.write("Hello file world!\n")
    f.close()


def read_file(file_name):
    f = open(file_name, 'r')
    return f.read()


create_file("myfile.txt")
print(read_file("myfile.txt"))
