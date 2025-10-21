import struct

def encode(n):
    """
    while n > 0 
        take lowest order 7 bits
        add the correct msb: 1 unless final 7 bits
        push to some sequence of bytes
    return byte sequence
    """
    out = []
    while n > 0:
        # if n == 0, then there are MSB signifying that there are more bit after processing this one.
        part = n & 0x7f
        # Imagine that we are done with the last bytes, and this will move it and handle the next sequence of byte.
        n >>= 7
        # This is for appending our MSB (if there are any)
        part |= (n and 0x80 or 0x00)
        out.append(part)
    return bytes(out)

def decode(varn):
    """
    for b in varn in reverse order:
        - discard msb
        - accumulate b
    """
    n = 0
    for b in reversed(varn):
        print(b)
        n <<= 7
        n += (b & 0x7f)
    return n

if __name__ == '__main__':
    cases = (
        ('1.uint64', b'\x01'),
        ('150.uint64', b'\x96\x01'),
        ('maxint.uint64', b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01'),
    )
    for fname, expectation in cases:
        with open(fname, 'rb') as file:
            n = struct.unpack('>Q', file.read())[0]
            assert encode(n) == expectation
            assert decode(encode(n)) == n
    print('ok')