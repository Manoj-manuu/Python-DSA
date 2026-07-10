# def maxArea(arr):
#     max_arr = 0
#     for i in range(len(arr) - 1):
#         for j in range(i+1, len(arr)):
#             newarr = min(arr[i],arr[j]) * (j - i)
#             max_arr = max(newarr,max_arr)
    
#     return max_arr
# print(maxArea([3,7,5,6,8,4]))

# O(n)
def maxArea(arr):
    maxAreaa = 0
    left = 0
    right = len(arr)-1
    while(left<right):
        newarr = min(arr[left],arr[right]) * (right - left)
        maxAreaa = max(newarr,maxAreaa)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    
    return maxAreaa
print(maxArea([3,7,5,6,9,8,4]))
