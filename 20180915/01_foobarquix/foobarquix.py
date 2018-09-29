def foobarquix(number):

    pattern = {
        3: "Foo",
        5: "Bar",
        7: "Quix"
    }

    value = ''.join([text for factor, text in pattern.items() if not number % factor])
    value += ''.join([text for digit in str(number) for factor, text in pattern.items() if digit == str(factor)])

    if not value:
        value = number

    return str(value)
