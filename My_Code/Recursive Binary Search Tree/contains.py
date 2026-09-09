class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def __r_insert(self,current_node,value):
        if current_node == None:
            return Node(value)

        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left,value)
        
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right,value)
        
        return current_node

    def r_insert(self,value):
        if self.root == None:
            self.root = Node(value)
        else:
            self.__r_insert(self.root,value)
        
    
    def __r_contains(self,current_node,value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left,value)
        if value > current_node.value:
            return self.__r_contains(current_node.right,value)

    def r_contains(self,value):
        return self.__r_contains(self.root,value)
    
    def __delete_node(self,current_node,value):
        if current_node == None:
            return None
        elif value < current_node.value:
            current_node.left = self.__delete_node(current_node.left,value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right,value)
        
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right,sub_tree_min)
                
        return current_node
    
    def delete_node(self,value):
        self.root = self.__delete_node(self.root, value)
        
        
    def min_value(self,current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

bst = BinarySearchTree()

# Insert
bst.r_insert(47)
bst.r_insert(21)
bst.r_insert(76)
bst.r_insert(18)
bst.r_insert(27)
bst.r_insert(52)
bst.r_insert(82)

# Contains
print("47:", bst.r_contains(47))
print("27:", bst.r_contains(27))
print("100:", bst.r_contains(100))

# Delete
bst.delete_node(18)
print("18 after delete:", bst.r_contains(18))

bst.delete_node(21)
print("21 after delete:", bst.r_contains(21))

bst.delete_node(76)
print("76 after delete:", bst.r_contains(76))
print("82:", bst.r_contains(82))