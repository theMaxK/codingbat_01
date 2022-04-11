def sum2(nums):
    if len(nums) >= 2: 
        result = nums[0] + nums[1]
        return result 
    else: 
        result = nums[0]
        return result 
    



print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))
