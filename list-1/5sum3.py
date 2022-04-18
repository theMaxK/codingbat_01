def sum3(a): 
    result = 0 
    for el in a: 
        result += el
    return result 

print(sum3([1, 2, 3]))
print(sum3([5, 11, 2]))
print(sum3([7, 0, 0]))
