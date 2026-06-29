class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):  #constructor
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

  # Printing list
  
    def printList(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

    #Append 
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length+= 1
        #return True

        
    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            prep = self.head

            while(temp.next):
                prep = temp
                temp = temp.next
            self.tail = prep
            self.tail.next = None
            self.length -= 1
             
            
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp # .value
        
    def prepend(self,value):
        newnode = Node(value)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head = newnode
            self.length += 1

    def popFirst(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next 
            temp.next = None
            self.length -=1 
            if self.length == 0:
                self.tail = None
            return temp.value

    

    def set_value(self,index,value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length :
            return self.append(value)
        newnode = Node(value)
        temp = self.get(index-1)
        newnode.next = temp.next
        temp.next = newnode

        
        
        self.length+=1
        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popFirst()
        if index == self.length -1 :
            return self.pop()
        prep = self.get(index - 1)
        temp = prep.next
        prep.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next =before
            before = temp
            temp = after

#print(My_linked_list.head.value)

My_linked_list = LinkedList(1)

My_linked_list.append(2)
My_linked_list.append(12)
My_linked_list.append(22)


# print(My_linked_list.pop())

# print(My_linked_list.pop())

# print(My_linked_list.pop())

# My_linked_list.prepend(3)
#My_linked_list.printList()

# print(My_linked_list.popFirst())
# print(My_linked_list.popFirst())
# print(My_linked_list.popFirst())

# print(My_linked_list.get(1))

# My_linked_list.set_value(1,4)
# My_linked_list.printList()

# My_linked_list.insert(1,23)
# My_linked_list.printList()

# My_linked_list.remove(1)
My_linked_list.printList()
My_linked_list.reverse()
print("/")
My_linked_list.printList()
