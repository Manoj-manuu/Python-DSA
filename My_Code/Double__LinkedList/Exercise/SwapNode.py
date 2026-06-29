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


    def swapNode(self):
        if self.head is None or self.head.next is None:
            return 
        
        dummy = Node(0)
        dummy.next = self.head
        self.head.prev = dummy
        prep = dummy

        while prep.next and prep.next.next:
            first = prep.next
            second = first.next

            first.next = second.next
            if second.next:
                second.next.prev = first

            second.next = first
            first.prev = second
            prep.next = second
            second.prev = prep

            prep = first
        self.head = dummy.next
        self.head.prev = None

My_Dll = DoubleLinkedList(1)
My_Dll.append(2)
My_Dll.append(3)
My_Dll.printList()

My_Dll.swapNode()
print(" ")
My_Dll.printList()

