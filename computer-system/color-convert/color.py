import sys
import re

d = dict(zip('0123456789abcdef', range(16)))
z = zip('0123456789abcdef', range(16))
print(list(z))

def xx_to_dec_alpha(xx):
    return ((d[xx[0]] << 4) + (d[xx[1]])) / 255

def xx_to_dec_color(xx):
    return (d[xx[0]] << 4) + (d[xx[1]])

def replace(match):
    # Since hex does not care if upper or lower
    hex = match.group(1).lower()
    if len(hex) in {3,4}:
        hex = ''.join(x + x for x in hex)
    dec_color = [xx_to_dec_color(hex[i:i+2]) for i in (0,2,4)]
    if len(hex) == 8:
        dec_alpha = xx_to_dec_alpha(hex[6:8])
        return f'rgba({" ".join(str(d) for d in dec_color)} / {dec_alpha:.5f})'
    return f'rgb({" ".join(str(d) for d in dec_color)})'
    

sys.stdout.write(re.sub(r'\#([0-9a-fA-F]+)', replace,sys.stdin.read()))