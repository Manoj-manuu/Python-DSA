class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    

class DoubleLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length  = self.length + 1

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next
    
    def partition(self,x):
        if self.length <= 0 or self.head is None:
            return None
        
        big_node = Node(0)
        small_node = Node(0)
        big = big_node
        small = small_node

        current = self.head
        
        while(current):
            
            next_node = current.next 
            
            current.next = None
            current.prev = None
            
            if current.value < x :
                small.next = current
                current.prev = small
                small = small.next
            else:
                big.next = current
                current.prev = big
                big = big.next
                
            current = next_node

        if small_node.next is not None:
            self.head = small_node.next
            small.next = big_node.next 
                
            if big_node.next is not None:
                
                big_node.next.prev = small
        else:
            small.next = None
        self.tail = big if big_node.next else small
        if self.head:
            self.head.prev = None

My_Dll = DoubleLinkedList(3)
My_Dll.append(8)
My_Dll.append(5)
My_Dll.append(10)
My_Dll.append(2)
My_Dll.append(1)

x =5
My_Dll.partition(x)
My_Dll.printList()




