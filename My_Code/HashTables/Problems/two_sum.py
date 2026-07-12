def two_sum(nums,target):
    seen={}
    for i,num in enumerate(nums):
        compound = target - num
        if compound in seen:
            return [seen[compound],i]
        else:
            seen[num] = i
    return []

print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))
print ( two_sum([], 0) )
print(two_sum([1,2,3,4,5],9))