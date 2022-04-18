def diff21(n): 
    abs_n = abs(n)
    if abs_n<=21: 
        return 21-abs_n
    else: 
        return (abs_n -21)*2

print(diff21(19))
print(diff21(10))
print(diff21(21))
    