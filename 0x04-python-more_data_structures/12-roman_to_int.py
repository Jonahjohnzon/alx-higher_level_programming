#!/usr/bin/python3
def subtraction(list_number):
    sub = 0
    max_list = max(list_number)

    for num in list_number:
        if max_list > num:
            sub += num
    return (max_list - sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0

    _numb = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    keys = list(_numb.keys())

    number = 0
    last_roman = 0
    list_number = [0]

    for char in roman_string:
        for r_number in keys:
            if r_number == char:
                if (_numb.get(char) <= last_roman):
                    number += subtraction(list_number)
                    list_number = [_numb.get(char)]
                else:
                    list_number.append(_numb.get(char))
                last_roman = _numb.get(char)

    number += subtraction(list_number)
    return (number)
