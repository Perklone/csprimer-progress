# Sample value from Wikipedia: 1789372997 (payload only)

def verify(digits):
    output = []
    multiplier = 1
    for digit in reversed(digits):
        multiplier = 1 if multiplier == 2 else 2
        multiplied = int(digit) * multiplier
        if multiplied > 9:
            multiplied_string = str(multiplied)
            output.append(int(int(multiplied_string[0]) + int(multiplied_string[1])))
                
        else:
            output.append(multiplied)

    combined = sum(output)
    result = (10 - (combined % 10))
    print(result)


if __name__ == '__main__':
    verify("1789372997")