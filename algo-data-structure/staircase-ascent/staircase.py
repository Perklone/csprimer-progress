def two_step_staircase(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b , a+b
    return a

def three_step_staircase(n):
    a, b, c = 1 , 1 , 2
    for _ in range(n):
        a, b, c = b, c, a+b+c
    return a
    

if __name__ == '__main__':
    val = 5
    print(f"Two step output of {val}: {two_step_staircase(val)}")
    print(f"Three step output of {val}: {three_step_staircase(val)}")
