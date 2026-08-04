class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def left_child(self,index):
        return 2 * index + 1
    
    def right_child(self,index):
            return 2 * index + 2
        
    def parent(self,index):
        return (index - 1)// 2
    
    def _swap(self,index1,index2):
        self.heap[index1],self.heap[index2] = self.heap[index2],self.heap[index1]
        
    
    def insert(self,value):
        self.heap.append(value)
        current = len(self.heap) - 1
        
        while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
            self._swap(current,self.parent(current))
            current = self.parent(current)
            
    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value  = self.heap[0]
        self.heap[0] = self.heap.pop()   
        self.sinkdown(0)
        return max_value
    
    def sinkdown(self,index):
    
        while True:
            
            max_index = index
            left_index = self.left_child(index)
            right_index = self.right_child(index)
            
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            
            if  right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
                
            if max_index != index:
                self._swap(index,max_index)
                index = max_index
            else:
                return 
    
def stream_max(nums):
    heap = MaxHeap()
    new_arr = []
    
    for num in nums:
        heap.insert(num)
        new_arr.append(heap.heap[0])
    
    return new_arr
    
test_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
    ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
]

for i, (nums, expected) in enumerate(test_cases):
    result = stream_max(nums)
    print(f'\nTest {i+1}')
    print(f'Input: {nums}')
    print(f'Expected Output: {expected}')
    print(f'Actual Output: {result}')
    if result == expected:
        print('Status: Passed')
    else:
        print('Status: Failed')


        
            
        
            