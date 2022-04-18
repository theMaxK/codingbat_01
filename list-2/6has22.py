def has22(nums): 

    for count ,number in enumerate(nums[:-1]): 
        print(count, number)
        if number==2 and nums[count+1] == 2: 
            return True 
         
    return False  

print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([2, 1, 2]))

