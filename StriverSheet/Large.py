def large(arr):
    large = arr[0]
    for i in range(len(arr)-1):
        if large < arr[i+1]:
            large = arr[i+1]
    return large

arr = [232,32,442,1,434,999]
print(large(arr))