class Dog:
    age_factor = 7

    def __init__(self, age):
        self.age = age
        Dog.validate(self.age)

    def human_age(self):
        data = round(self.age_factor * self.age)
        return data

    def validate(self):
        if isinstance(self, int):
            return self
        else:
            raise ValueError
