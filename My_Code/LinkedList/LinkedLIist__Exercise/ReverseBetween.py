class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

    def printList(self):
        temp = self.head
        while(temp is not None):
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.lenght += 1

    def reverseBetween(self, start_index, end_index):

        if self.head is None or self.head.next is None:
            return

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

    # Step 1: Move prev to node BEFORE start_index
        for _ in range(start_index):
            prev = prev.next

        current = prev.next

    # Step 2: Reverse the sublist
        for _ in range(end_index - start_index):
            to_move = current.next
            current.next = to_move.next
            to_move.next = prev.next
            prev.next = to_move

        self.head = dummy.next




ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
start_index =2
end_index = 4
ll.reverseBetween(start_index, end_index)
ll.printList()
