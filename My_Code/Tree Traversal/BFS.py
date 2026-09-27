def bfs(self):
    current_node = self.root
    queue = []
    result = []
    queue.append(current_node)
    
    while len(queue) > 0:
        current_node = queue.pop(0)
        result.append(current_node.value)
        
        if current_node.left is not None:
            queue.append(current_node.left)
        
        if current_node.right is not None:
            queue.append(current_node.right)
        
    return result

def dfs_preorder(self):
    results = []
    
    def traverse(self,current_node):
        results.append(current_node.value)
        
        if current_node.left is not None:
            traverse(current_node.left)
            
        if current_node.right is not None:
            traverse(current_node.right)
            
    traverse(self.root)
    return results

def dfs_postorder(self):
    results = []
    
    def traverse(self,current_node):
    
        if current_node.left is not None:
            traverse(current_node.left)
            
        if current_node.right is not None:
            traverse(current_node.right)
        
        results.append(current_node.value)
            
    traverse(self.root)
    return results

def dfs_inorder(self):
    results = []
    
    def traverse(self,current_node):
        
        if current_node.left is not None:
            traverse(current_node.left)
            
        results.append(current_node.value)
            
        if current_node.right is not None:
            traverse(current_node.right)
            
    traverse(self.root)
    return results


    
    