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
        
    def removeDup(self):
        current  = self.head 
        while current:
            runner = current
            while runner.next :
                if runner.next.value == current.value:
                    runner.next = runner.next.next
                    self.length -= 1
                else:
                    runner = runner.next
            current = current.next
        
        

            

My_LinkedList = LinkedList(1) 
My_LinkedList.append(2)
My_LinkedList.append(3)
My_LinkedList.append(1)
My_LinkedList.append(4)
My_LinkedList.append(2)
My_LinkedList.append(5)
My_LinkedList.printList()
print("\n")

My_LinkedList.removeDup()
My_LinkedList.printList()



