class Stack:
    def __init__(self):
        self.stack_list = []
    
    def printList(self):
        for i in range(len(self.stack_list)-1,-1,-1):
            print(self.stack_list[i])
    
    def push(self,value):
        self.stack_list.append(value)
    
    def pop(self):
        if len(self.stack_list) == 0:
            return None    
        return self.stack_list.pop()
    
    def is_empty(self):
        return len(self.stack_list) == 0
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]
    
def reverse_string(word):
    my_stack = Stack()

    for ch in word:
        my_stack.push(ch)
    
    rev = " "
    while not my_stack.is_empty():
        rev += my_stack.pop()
    
    return rev

# def balance_paranthasis(mystring):
#     stack = Stack()

#     for ch in mystring:
#         if ch == "(":
#             stack.push(ch)
#         elif ch == ")":
#             if stack.is_empty():
#                 return None
#             else:
#                 stack.pop()
#     return stack.is_empty()

# def sort_stack(mystack):
#     sorted_stack = Stack()

#     while not mystack.isempty():
#         temp = mystack.pop()

#         while (not sort_stack.isempty() and sort_stack.peek() > temp):
#             my_stack.push(sort_stack.pop())
#         sort_stack.push(temp)

#     while not sort_stack.isempty():
#         mystack.push(sort_stack.pop())
#     return my_stack




my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print(reverse_string("man"))


