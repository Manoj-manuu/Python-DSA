class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
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
            self.tail = new_node
        self.length += 1

    def printList(self):
        temp = self.head
        while(temp is not None):
            print(temp.value)
            temp = temp.next
    
    
    def partition(self,x):
        if self.head is None:
            return None
        dummy_big = Node(0)
        dummy_small = Node(0)
        
        small = dummy_small
        big = dummy_big
        current = self.head
        while(current):
            if current.value < x:
                small.next = current
                small = small.next
            else:
                big.next = current
                big = big.next
            current = current.next
        big.next = None
        small.next = dummy_big.next
        self.head =dummy_small.next

        

My_LinkedList = LinkedList(3)
My_LinkedList.append(8)
My_LinkedList.append(5)
My_LinkedList.append(10)
My_LinkedList.append(2)
My_LinkedList.append(1)



x = 5
My_LinkedList.partition(x)
My_LinkedList.printList()