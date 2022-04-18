def centered_average(nums): 
    maxx = max(nums)
    minn = min(nums)
    nums.remove(maxx)
    nums.remove(minn)
    lenn = len(nums)
    result = 0 
    for el in nums: 
        result += el
    
    return int(result/ lenn)

    


print(centered_average([1,2,3,4,100]))
print(centered_average([1,1,5,5,10,8,7]))
print(centered_average([-10,-4,-2,-4,-2,0]))
