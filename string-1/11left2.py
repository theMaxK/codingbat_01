from turtle import left


def left2(str):
    if len(str) > 2:
        return str[2:]+str[:2]
    else:
        return str


print(left2('Hello'))
print(left2('java'))
print(left2('Hi'))
