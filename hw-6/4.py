class ValidationMixin:

    def validate(self, list_int):
        if not isinstance(list_int, list):
            raise TypeError
        elif not all(isinstance(x, int) for x in list_int):
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
                if (i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0) and (i > 0):
                    print(i)
                    data.append(i)
            return data


class Mathematician(FilterLeaps, RemovePositives, SquareNums):
    pass


if __name__ == "__main__":
    m = Mathematician()

    assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
    assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]