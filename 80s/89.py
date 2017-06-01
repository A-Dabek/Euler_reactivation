def roman_to_numeric(roman):
    max_found = roman_dict[roman[-1]]
    number = 0
    for i in reversed(range(len(roman))):
        temp = roman_dict[roman[i]]
        if temp > max_found:
            max_found = temp
        if temp < max_found:
            temp = -temp
        number += temp
    return number


def numeric_to_minimal_roman(number):
    roman = ''
    while number >= 1000:
        roman += 'M'
        number -= 1000
    if number >= 900:
        roman += 'CM'
        number -= 900
    if number >= 500:
        roman += 'D'
        number -= 500
    if number >= 400:
        roman += 'CD'
        number -= 400
    while number >= 100:
        roman += 'C'
        number -= 100
    if number >= 90:
        roman += 'XC'
        number -= 90
    if number >= 50:
        roman += 'L'
        number -= 50
    if number >= 40:
        roman += 'XL'
        number -= 40
    while number >= 10:
        roman += 'X'
        number -= 10
    if number == 9:
        roman += 'IX'
        number -= 9
    if number >= 5:
        roman += 'V'
        number -= 5
    if number == 4:
        roman += 'IV'
        number -= 4
    while number > 0:
        roman += 'I'
        number -= 1
    return roman


file = open('res/89.txt')

roman_numerals = file.read().split('\n')

roman_dict = {'I': 1,
              'V': 5,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000}

evaluated = [roman_to_numeric(i) for i in roman_numerals]
minimal = [numeric_to_minimal_roman(i) for i in evaluated]
print(roman_numerals)
print(evaluated)
print(minimal)

sum_of_roman = 0
sum_of_minimal = 0
for i in range(len(roman_numerals)):
    sum_of_roman += len(roman_numerals[i])
    sum_of_minimal += len(minimal[i])
print(sum_of_roman, sum_of_minimal, sum_of_roman-sum_of_minimal)
