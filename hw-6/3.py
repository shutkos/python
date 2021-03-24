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