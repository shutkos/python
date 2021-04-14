# Напишіть клас Ball(color:str) з інформативними методами __repr__ та __str__.

class Ball:
    def __init__(self, color: str):
        self.color = color

    def __str__(self):
        return f"<Color: {self.color}>"

    def __repr__(self):
        return 'Object: {}'.format(self.color)


ball = Ball("green")
print(ball.__str__())
print(ball.__repr__())