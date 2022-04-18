def parrot_trouble(talking, hour):
    if hour < 7 or hour > 20:
        if talking == True:
            return True
        else:
            return False
    else:
        return False


print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))
