def in1to10(n,outside_mode):
    
    if outside_mode == False: 
        if n in range(1,11):
            return True 
        else:
            return False 
    elif outside_mode == True: 
        if n == 1 or n >= 10: 
            return True 
    else: 
        False  

    

print(in1to10(5, False))
print(in1to10(11, False))
print(in1to10(11, True))