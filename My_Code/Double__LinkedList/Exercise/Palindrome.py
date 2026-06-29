class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
class LinkedList:
    def __init__(self,value):
        newnode = Node(value)
        self.head = newnode
        self.tail = newnode
        self.lenght =+ 1
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next
    
    def append(self,value):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        
        else:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
        self.length =+ 1
        
    def pop(self):
        if self.length is None or self.head is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail =None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.lenght -= 1
        return temp.value
    
    def is_palindrome(self):
        if self.lenght <=1:
            return True
        
        forward = self.head
        backward = self.tail

        for _ in range(self.lenght//2):

            if forward.value != backward.value:
                return False
            
            forward = forward.next
            backward = backward.next
        return True

        
    
        
        
        
ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
print(ll.is_palindrome())
