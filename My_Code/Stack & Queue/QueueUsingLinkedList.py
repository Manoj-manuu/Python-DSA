class Node:
    def __init__(self,value):
        self.value = value
        self.next  = None
    

class queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.height = 1

    def printQueue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self,value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.height += 1

    def dequeue(self):
        if self.height == 0:
            return None
        temp = self.first
        if self.height == 1 or self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.height -= 1
        return temp.value
    
My_Queue = queue(1)
My_Queue.enqueue(2)
My_Queue.enqueue(3)
My_Queue.enqueue(4)
My_Queue.printQueue()


print("Removed : ",My_Queue.dequeue())
print("Removed : ",My_Queue.dequeue())
print("Removed : ",My_Queue.dequeue())
print("Removed : ",My_Queue.dequeue())

My_Queue.printQueue()
        