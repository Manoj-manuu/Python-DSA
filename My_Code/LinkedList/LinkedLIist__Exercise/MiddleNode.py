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
        
    def middle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value
    
  
        

My_LinkedList = LinkedList(1)
My_LinkedList.append(2)
My_LinkedList.append(3)
My_LinkedList.append(4)
My_LinkedList.append(5)
My_LinkedList.append(6)
My_LinkedList.append(7)
My_LinkedList.append(8)
My_LinkedList.append(9)
My_LinkedList.append(10)
My_LinkedList.printList()

print("The middle node is : ",My_LinkedList.middle())

