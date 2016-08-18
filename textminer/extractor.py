import re


def phone_number(data):
    if re.search(r'.*\d{3}.*\d{3}.*\d{4}', data):
        return True
