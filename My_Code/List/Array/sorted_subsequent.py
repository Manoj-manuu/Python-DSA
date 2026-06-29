#You are given an array of Integers in which each subsequent value is not less than the previous value. 
# Write a function that takes this array as an input and returns a new array with the squares of each number sorted in ascending order.

def sorted_square(arr1):
    i = 0
    j = len(arr1) - 1
    newarr = [0] * len(arr1)

    for k in reversed(range(len(arr1))):

        sq_i = arr1[i] * arr1[i]
        sq_j = arr1[j] * arr1[j]

        if sq_i > sq_j:
            newarr[k] = sq_i
            i = i + 1
        else:
            newarr[k] = sq_j
            j = j - 1

    return newarr
arr1 = [-8,-1,3,4,7]
print(sorted_square(arr1))

