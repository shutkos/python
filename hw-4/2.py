# Створіть функцію make_country, яка приймає назву країни та її столицю як параметри. П
# отім створіть словник з цих параметрів, де name і capital будуть ключами, і поверніть цей словник.
# Також додайте додаткову валідацію введених параметрів, оскільки вони повинні бути рядками.
# Якщо переданий параметр неправильного типу, має викликатись помилка TypeError з відповідним повідомленням.
# Створіть іншу функцію під назвою show_country_info, яка приймає словник і повертає рядок в такому форматі —
# "Country: {country}, Capital: {capital}." У кінці програми запринтіть виведення функції show_country_info,
# яка приймає на вхід результат виконання функції make_country, викликаної з параметрами "Gondor" і "Minas Tirith".
def make_country(country_name, capital_name):
    if isinstance(country_name, str) and isinstance(capital_name, str):
        dictionary = {'name': country_name, 'capital': capital_name}
        return dictionary
    else:
        raise ValueError


def show_country_info(country_dict):
    name = country_dict['name']
    capital = country_dict['capital']
    data = "Country: {}, Capital: {}.".format(name, capital)
    return data


print(show_country_info(make_country('Gondor', 'Minas Tirith')))