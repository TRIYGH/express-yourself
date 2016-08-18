import re


def binary(data):
    return re.match(r'[01]', data)


def binary_even(data):
    if re.match(r'.+0$', data):
        if binary(data):
            return True


def hex(data):
    return re.match(r'[0-9A-F][^G-Z][^a-z]', data)


def word(data):
    if re.match(r'.*[^0-9].*', data):
        if re.match(r'[^!+]', data):
            if not re.search(r'[*]', data):
                return True


def words(data, **ct):
    if data == '':
        return False
    check_data = word(data)
    how_split = re.compile(r' [^ !+]').split(data)
    count = len(how_split)
    if check_data:
        return True, count
    else:
        return False, count


def phone_number(data):
    if re.search(r'.*\d{3}.*\d{3}.*\d{4}', data):
        return True


def money(data):
    if re.match(r'^\${1}(\d*(\d\.?|\.\d{0,2}))$', data):
            return True
    # if re.match(r'.*[,\d{3}]', data):
    #     num = data.split('.')
    #     num_commas = num[0].split(',')
    #     i = len(num_commas)
    #     for all in range(1, i):
    #         if len(num_commas[all]) != 3:
    #             return False


def zipcode(data):
    if len(data) > 5:
        x = list(data)
        if x[5] != '-':
            return False
        elif len(data.split('-')[1]) != 4:
            return False

    if re.search(r'(\d{5}){1}(-\d{4})?', data):
        return True


def date(data):
    if re.match(r'\d{4}', data[:4]):
        dat = data[5:] + '-' + data[:4]
        data = dat
    if re.match(r'\d{1,2}.\d{1,2}.\d{4}', data):
        return True
