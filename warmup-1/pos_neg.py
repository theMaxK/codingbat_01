def pos_neg(a, b, negative):

    if (a > 0 and b < 0) or (b > 0 and a < 0):
        return True
    elif negative == True:
        if (a < 0 and b < 0):
            return True
    else:
        return False


print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))
