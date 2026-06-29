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


    def reverseDll(self):
        if self.head is None: #self.length <= 0
            return None
        
        current = self.head

        while(current):
            before = current.prev
            current.prev = current.next
            current.next = before
            current = current.prev

        self.head,self.tail = self.tail,self.head

My_Dll = DoubleLinkedList(1)
My_Dll.append(2)
My_Dll.append(3)
My_Dll.printList()

My_Dll.reverseDll()
print(" ")
My_Dll.printList()

