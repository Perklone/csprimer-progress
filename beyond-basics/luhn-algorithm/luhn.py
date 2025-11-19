# Sample value from Wikipedia: 1789372997 (payload only)

LOOKUPS = (
    dict(zip('0123456789', (0,1,2,3,4,5,6,7,8,9))),
    dict(zip('0123456789', (0,2,4,6,8,1,3,5,7,9))),
)

def verify_imperative(digits):
    total = 0
    for i, d in enumerate(reversed(digits)):
        total += LOOKUPS[i%2][d]
    
    return total % 10 == 0

def verify_functional(digits):
    return sum(LOOKUPS[i%2][d] for i, d in enumerate(reversed(digits))) % 10 == 0

if __name__ == '__main__':
    for verify in (verify_imperative, verify_functional):
        assert verify("17893729974")
        assert not verify("17893729975")
        print(verify.__name__ + " ok")