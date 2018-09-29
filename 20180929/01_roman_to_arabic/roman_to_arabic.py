def roman_to_arabic(roman_number):
    r2a_table = {
        "I":	1,
        "V":	5,
        "X":	10,
        "L":	50,
        "C":	100,
        "D":	500,
        "M":	1000
    }

    value = 0

    for index, roman_digit in enumerate(roman_number):
        try:
            if r2a_table[roman_digit] >= r2a_table[roman_number[index+1]]:
                value += r2a_table[roman_digit]
            else:
                value -= r2a_table[roman_digit]
        except IndexError:
            value += r2a_table[roman_digit]

    return value
