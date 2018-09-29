def roman_validator(roman_number):
    digit_valid_reps = {
        "I":    3,
        "V":    1,
        "X":    3,
        "L":    1,
        "C":    3,
        "D":    1,
        "M":    3
    }

    not_valid = ["IL", "ID", "IM", "XD", "XM", 
                 "VX", "VL", "VC", "VD", "VM",
                 "LC", "LD", "LM",
                 "DM"]

    for digit, reps in digit_valid_reps.items():
        if roman_number.count(digit) > reps:
            return False

    for item in not_valid:
        if roman_number.find(item) != -1:
            return False

    return True
