class BinarySearchTree:

    def __r_contains(self,current_node,value):
        if current_node == None:
            return False
        if value == current_node:
            return True
        if value < current_node:
            return __r_contains(self,current_node.left,value)
        if value > current_node:
            return __r_contains(self,current_node.right,value)

    def r_contains(self,value):
        return __r_contains(self.root,value)

my_tree = BinarySearchTree()
my_tree.insert(45)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.r_contains(27))

        