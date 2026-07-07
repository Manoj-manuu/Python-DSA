def find_duplicate(nums):
    seen = {}
    for num in nums:
        seen[num] = seen.get(num,0) + 1
    
    duplicate = []
    for num, count in seen.items():
        if count > 1:
            duplicate.append(num)
    return duplicate

nums = []
print(find_duplicate(nums))