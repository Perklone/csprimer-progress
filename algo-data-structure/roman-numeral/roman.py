values = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

def roman_numeral(n):
    for val, symbol in values:
        if n == 0:
            return ""
        if n >= val:
            return symbol + roman_numeral(n-val)

if __name__ == '__main__':
    print(roman_numeral(39))
    print(roman_numeral(246))
    print(roman_numeral(789))
    print(roman_numeral(2421))
    print(roman_numeral(2026))
