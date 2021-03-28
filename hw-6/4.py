# Реалізуйте клас Mathematician, який буде допоміжним класом для проведення математичних операцій над списком цілих
# чисел. Клас не приймає жодних атрибутів і має тільки методи:
# (1) square_nums (приймає список цілих чисел і повертає список їхніх квадратів);
# (2) remove_positives (приймає список цілих чисел і повертає його без додатних чисел);
# (3) filter_leaps (приймає список років (цілих чисел) і прибирає невисокосні).
# Ці методи мають бути не визначені безпосередньо в цьому класі, а отримані за допомогою наслідування з трьох базових
# класів із цими методами. Іншими словами, потрібно створити три окремі класи, які інкапсулюють описану логіку, але
# клас Mathematician потримує її через наслідування. Також потрібно створити окремий клас, який валідує параметр,
# переданий у методи. Має викликатися TypeError, якщо параметр не є списком, і ValueError, якщо переданий список не
# є списком цілих чисел.
class ValidationMixin:

    def validate(self, list_int):
        if not isinstance(list_int, list):
            raise TypeError
        elif not isinstance(list_int, int):
            raise ValueError
        else:
            return True


class SquareNums(ValidationMixin):

    def square_nums(self, list_int):
        if self.validate(list_int):
            data = [i ** 2 for i in list_int]
            return data


class RemovePositives(ValidationMixin):

    def remove_positives(self, list_int):
        if self.validate(list_int):
            data = []
            for i in list_int:
                if i < 0:
                    data.append(i)
            return data


class FilterLeaps(ValidationMixin):

    def filter_leaps(self, list_int):
        if self.validate(list_int):
            data = []
            for i in list_int:
                if (i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0):
                    data.append(i)
            return data


class Mathematician(FilterLeaps, RemovePositives, SquareNums):
    pass


if __name__ == "__main__":
    m = Mathematician()

    assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
