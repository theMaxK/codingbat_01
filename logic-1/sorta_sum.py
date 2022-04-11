def sorta_sum(a,b): 
    new_sum = a+b 
    if new_sum >= 10 and new_sum <=19: 
        return 20
    else: 
        return new_sum
    

print(sorta_sum(3,4))
print(sorta_sum(9,4))
print(sorta_sum(10,11))