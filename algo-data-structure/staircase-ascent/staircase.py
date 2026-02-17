def two_step_staircase(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else: return two_step_staircase(n - 2) + two_step_staircase(n-1)

def three_step_staircase(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else: return three_step_staircase(n-1) + three_step_staircase(n-2) + three_step_staircase (n-3)
    

if __name__ == '__main__':
    val = 5
    print(f"Two step output of {val}: {two_step_staircase(val)}")
    print(f"Three step output of {val}: {three_step_staircase(val)}")
