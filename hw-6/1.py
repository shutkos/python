class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_greeting(self):
        greeting = "Hello, my name is {} {} and I’m {} years old".format(self.first_name, self.last_name, self.age)
        return greeting

    def talk(self):
        print(self.get_greeting())