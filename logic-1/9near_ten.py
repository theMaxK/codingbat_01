def near_ten(num): 
    if num%10 <= 2: 
        return True 
    elif num%10 >=8 and num%10 <10: 
        return True 
    else: 
        return False 

print(near_ten(12))
print(near_ten(17))
print(near_ten(19))
