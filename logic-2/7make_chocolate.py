def make_chocolate(small, big, goal): 
    s = small 
    b = big *5
    

    if goal >= b: 
        remainder = goal-b 
    else: 
        remainder = goal%5

    if remainder <= s: 
        return remainder
    
    return -1 
   



print(make_chocolate(4,1,9))
print(make_chocolate(4,1,10))
print(make_chocolate(4,1,7))