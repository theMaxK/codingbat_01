def sum13(nums):

    while 13 in nums:

        if nums.index(13) < len(nums)-1:
            nums.pop(nums.index(13)+1)
        nums.pop(nums.index(13))

    return sum(nums)


print(sum13([1, 2, 2, 1]))
print(sum13([1, 1, 14]))
print(sum13([1, 2, 2, 1, 13]))
print(sum13([13, 1, 13]))

## credits to https://github.com/diezguerra/codingbat-python-solutions/blob/master/list-2.py
