class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self,value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1

    def append(self,value):
        newnode = Node(value)

        if self.head is None:
            self.head = newnode
            self.tail = newnode
        
        else:
             self.tail.next = newnode
             newnode.prev = self.tail
             self.tail = self.tail.next

        self.length += 1
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next
    
    def reverse_between(self,start,end):
        if not self.head or start == end:
            return None
        
        dummy = Node(0)
        dummy.next = self.head
        prep = dummy
        
        for _ in range(start):
            prep = prep.next

        current = prep.next

        for _ in range( end- start):

            to_move = current.next
            current.next = to_move.next

            if to_move.next:
                to_move.next.prev = current

            to_move.next = prep.next
            prep.next.prev = to_move

            prep.next = to_move
            to_move.prev = prep
            

        self.head = dummy.next
        self.head.prev = None

        temp =self.head
        while(temp):
            temp = temp.next
        self.tail = temp

myDll = DoubleLinkedList(1)
myDll.append(2)
myDll.append(3)
myDll.append(4)
myDll.append(5)            
myDll.printList()
start = 1
end = 3
myDll.reverse_between(start,end)
print(" ")
myDll.printList()
        