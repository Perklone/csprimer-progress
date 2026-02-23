def my_binary_search(arr, val):
    low = 0
    hi = len(arr)

    while(low < hi):
        index = (low + hi) // 2
        if low == hi:
            break

        if arr[index] == val:
            return index
        elif arr[index] > val:
            hi = index
        elif arr[index] < val:
            low = index + 1
    return None


if __name__ == '__main__':
    a = (0,1,3,4)
    b = (-5,-2,0)

    cases = (
    # find in any position, even size
    (a, 0, 0),
    (a, 1, 1),
    (a, 3, 2),
    (a, 4, 3),
    # find in any position, odd size
    (b, -5, 0),
    (b, -2, 1),
    (b, 0, 2),
    # fail to find
    (a, 2, None),
    (b, -3, None),
)
    for nums, n, exp in cases:
        assert my_binary_search(nums, n) == exp, f"When we search for {n}: {my_binary_search(nums, n)} is not the same as {exp}"
    print("IS OK")