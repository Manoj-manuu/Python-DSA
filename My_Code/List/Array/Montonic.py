def monotonic_array(array):
    increase  = True
    decrease = True

    for i in range(len(array) -1 ):
        if array[i] > array[i+1]:
            increase = False
        if array[i] < array[i +1]:
            decrease = False
    
    return True or False
 
    
array = [1,2,3]
print(monotonic_array(array))