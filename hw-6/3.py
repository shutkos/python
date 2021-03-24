# Створіть класову структуру на Python, яка представляє людей в школі. Почніть з базового класу Person, потім класу
# Student і ще одного класу Teacher. Є список атрибутів, які можуть бути присвоєні цим класам: first_name, last_name,
# birth_date, university, course, salary. Стежте за тим, які атрибути загальні, а які – ні. Наприклад, first_name
# повинен бути атрибутом Person, а university не може за замовчуванням відноситись до Person і, швидше за все, буде
# атрибутом Student, який є дочірнім класом Person. Ще одне обмеження для цього завдання в тому, що кожен клас повинен
# ініціалізуватися тільки зі значеннями за замовчуванням "N/A" і кожен атрибут повинен присвоюватися через спеціальний
# метод-сетер. Наприклад, клас Person повинен мати спеціальний метод set_first_name(self, first_name), який присвоює
# переданий параметр до атрибута first_name екземпляра класу:
# Також наші класи повинні мати обмеження на зберігання тільки рядків у нижньому регістрі як атрибутів. Якщо в сетер
# переданий об'єкт іншого типу, має викликатися TypeError з повідомленням "Class is working with strings only", а
# передані рядки мають переводитися в нижній регістр перед присвоєнням до атрибутів екземплярів класів
# Person/Student/Teacher.
class Person:
    def __init__(self, first_name="N/A", last_name="N/A", birth_date="N/A"):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def set_first_name(self, first_name):
        if isinstance(first_name, str):
            self.first_name = first_name.lower()
        else:
            raise ValueError("Class is working with strings only")

    def set_last_name(self, last_name):
        if isinstance(last_name, str):
            self.last_name = last_name.lower()
        else:
            raise ValueError("Class is working with strings only")

    def set_birth_date(self, birth_date):
        if isinstance(birth_date, str):
            self.birth_date = birth_date
        else:
            raise ValueError("Class is working with strings only")


class Student(Person):
    def __init__(self, first_name="N/A", last_name="N/A", birth_date="N/A", university="N/A", course="N/A"):
        super().__init__(first_name, last_name, birth_date)
        self.university = university
        self.course = course

    def set_university(self, university):
        if isinstance(university, str):
            self.university = university.lower()
        else:
            raise ValueError("Class is working with strings only")

    def set_course(self, course):
        if isinstance(course, str):
            self.course = course.lower()
        else:
            raise ValueError("Class is working with strings only")


class Teacher(Student):
    def __init__(self, first_name="N/A", last_name="N/A", birth_date="N/A", university="N/A", salary="N/A"):
        super().__init__(first_name, last_name, birth_date, university)
        self.salary = salary

    def set_salary(self, salary):
        if isinstance(salary, str):
            self.salary = salary.lower()
        else:
            raise ValueError("Class is working with strings only")