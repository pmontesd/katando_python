def arabic_to_roman(arabic_number):
    a2r_table = {
        1:    "I",
        5:    "V",
        9:    "IX",
        10:   "X",
        50:   "L",
        90:   "XC",
        100:  "C",
        500:  "D",
        900:  "CM",
        1000: "M"
    }
    basex4_table = {
        1:    "IV",
        10:   "XL",
        100:  "CD",
        1000: "CM"
    }

    roman = ""
    value = arabic_number
    for index, base in enumerate(sorted(a2r_table.keys(), reverse=True)):
        cardinal = value // base
        value = value % base
        if a2r_table[base] in ("I", "X", "C", "M") and cardinal > 3:
            roman += basex4_table[base]
            continue
        roman += a2r_table[base]*cardinal
    return roman


