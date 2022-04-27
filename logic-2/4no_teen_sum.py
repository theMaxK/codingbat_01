from sre_parse import fix_flags
from numpy import fix


def no_teen_sum(a, b, c):
    return fix_teen(a)+fix_teen(b)+fix_teen(c)


def fix_teen(n):
    if 13 <= n and n <= 19 and n != 15 and n != 16:
        return 0
    return n


print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))
