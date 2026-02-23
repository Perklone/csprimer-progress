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

def roman_numeral_recursive(n):
    if n == 0:
        return ""
    for val, sym in values:
        if n >= val:
            return sym + roman_numeral_recursive(n-val)

def roman_numeral(n):
    val = ""
    while n != 0:
        for v,k in values:
            if n >= v:
                n-=v
                val+=k
                break
    return val

            
        

if __name__ == '__main__':
    print(roman_numeral(39))
    print(roman_numeral_recursive(39))
    print(roman_numeral(246))
    print(roman_numeral_recursive(246))
    print(roman_numeral(789))
    print(roman_numeral_recursive(789))
    print(roman_numeral(2421))
    print(roman_numeral_recursive(2421))
    print(roman_numeral(2026))
    print(roman_numeral_recursive(2026))
