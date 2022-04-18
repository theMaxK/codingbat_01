def love6(a, b):
    abs_a = abs(a)
    abs_b = abs(b)
    sum_ab = abs_a + abs_b
    diff_ab = abs_a - abs_b
    diff_ba = abs_b - abs_a

    if a == 6:
        return True
    if b == 6:
        return True

    elif sum_ab == 6 or diff_ab == 6 or diff_ba == 6:
        return True
    else:
        return False


print(love6(6, 4))
print(love6(4, 5))
print(love6(1, 5))
