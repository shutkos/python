# Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) з належною
# перевіркою й обробкою помилок.

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        new_num = (self.num * other.den + self.den * other.num)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num / other.num
        new_den = self.den / other.den
        return Fraction(new_num, new_den)

    def __str__(self):
        return 'Fraction({}, {})'.format(self.num, self.den)

    def __repr__(self):
        return "Fraction('" + self.den + "', " + self.num + ")"

    def __eq__(self, other):
        return self.num == other.den


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)
