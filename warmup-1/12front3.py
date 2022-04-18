def front3(str):
    if len(str) <= 3:
        return str*3
    return_str = str[0:3]
    
    return return_str*3

print(front3('Java'))
print(front3('Chocolate'))
print(front3('abc'))