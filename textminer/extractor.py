import re


def phone_numbers(data):
    return re.findall(r'.?\d{3}.*\d{3}.*\d{4}', data)
