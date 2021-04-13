# Створіть власний виняток під назвою CustomException. Можна успадкувати від базового класу Exception, але розширте
# його функціональність так, щоб він приймав спеціальний іменний аргумент file_log_msg, який повинен логуватися до
# файлу logs.txt. Якщо жоден параметр file_log_msg не переданий, використовуйте перший позиційний аргумент як
# стандартне значення. В іншому випадку пропустіть логування до файлу.
# Підказка: використовуйте метод __init__ для розширення функціоналу збереження повідомлень до файлу.

class CustomException(Exception):
    _file = "logs.txt"

    def __init__(self, *args, file_log_msg='', **kwargs):

        if (file_log_msg == '') and (len(self.args) > 0):
            msg = args[0]
            with open(self._file, 'a') as file:
                file.write(msg + '\n')
                file.close()

        if file_log_msg != '':
            with open(self._file, 'a') as file:
                file.write(file_log_msg + '\n')
                file.close()

        super().__init__(file_log_msg)


if __name__ == "__main__":
    raise CustomException("Hello")
