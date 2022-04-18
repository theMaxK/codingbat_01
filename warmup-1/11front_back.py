def front_back(str): 
    if len(str) <= 1: 
        return str
    first_letter = str[0]
    last_letter = str[-1]
    
    return last_letter + str[1:-1] + first_letter

print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
