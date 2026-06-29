# def rotateArray(arr,k):
#     n = len(arr)
#     j = n - k
#     i = 0
#     k = k % n
#     newarr = []
#     for _ in range(k):
#         newarr.append(arr[j])
#         j += 1
#     for _ in range(n - k):
#         newarr.append(arr[i])
#         i = i + 1
#     return newarr

# arr=[1,2,3,4]
# k = 5
# print(rotateArray(arr,k))

def rotateArray(array,k):
    n = len(array)
    k = k % n
    reverseArray(array,0,len(array)-1)
    reverseArray(array,0,k - 1)
    reverseArray(array,k,len(array)-1)
    return array
def reverseArray(array,start,end):
    while start < end :
        array[start],array[end] = array[end],array[start]
        start += 1
        end -= 1
    return array

print(rotateArray([1,2,3,4,5],3))