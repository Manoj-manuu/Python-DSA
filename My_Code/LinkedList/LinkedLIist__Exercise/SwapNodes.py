class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.length = 1


    def printList(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            self.length = 1
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.length += 1

   
    def swap_pairs(self):
        if self.head is None or self.head.next is None:
            return

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

        
            prev.next = second
            first.next = second.next
            second.next = first

       
            prev = first

        self.head = dummy.next


ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)


ll.swap_pairs()
ll.printList()