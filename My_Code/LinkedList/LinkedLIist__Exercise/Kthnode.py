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
    

def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head

    # Step 1: move fast k steps ahead
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next

    # Step 2: move both pointers
    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow
        
        

My_LinkedList = LinkedList(1)
My_LinkedList.append(2)
My_LinkedList.append(3)
My_LinkedList.append(4)
My_LinkedList.printList()

k = 3
result = find_kth_from_end(My_LinkedList, k)

if result:
    print(result.value)
else:
    print(None)