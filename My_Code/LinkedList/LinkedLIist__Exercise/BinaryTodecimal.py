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
    
    
    def binaryTodecimal(self):
        current = self.head
        result = 0
        while current:
            result = result*2 + current.value
            current = current.next
        return result
        

My_LinkedList = LinkedList(1)
My_LinkedList.append(1)
My_LinkedList.append(1)
My_LinkedList.append(1)


print(My_LinkedList.binaryTodecimal())

My_LinkedList1 = LinkedList(1)
My_LinkedList1.append(1)
My_LinkedList1.append(0)
My_LinkedList1.append(0)
print(My_LinkedList1.binaryTodecimal())
