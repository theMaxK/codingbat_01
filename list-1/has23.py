def has23(nums): 
    for _ in nums: 
        if 2 in nums: 
            return True 
        elif 3 in nums: 
            return True 
        else: 
            return False 
            
                

print(has23([4,4]))
