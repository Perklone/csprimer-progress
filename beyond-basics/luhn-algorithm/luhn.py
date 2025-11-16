# Sample value from Wikipedia: 1789372997 (payload only)

def verify(digits):
    sum = 0
    for index, digit in enumerate(digits[-2::-1]):
        multiplied = int(digit) * (2 - index % 2)
        sum += multiplied // 10 + multiplied % 10

    result = (10 - (sum % 10))
    return result == int(digits[-1])

if __name__ == '__main__':
    assert verify("17893729974")
    assert not verify("17893729975")