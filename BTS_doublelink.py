class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = Node(value)
                node.left.parent = node
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = Node(value)
                node.right.parent = node
    
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)
    
    def tree_search(self, k):
        current = self.root
        while current and current.value != k:
            if k < current.value:
                current = current.left
            else:
                current = current.right
        return current
    
    def _min_node(self, node): #leftest of the subtree
        min = node
        while min and min.left:
            min = min.left
        return min
    
    def successor(self, node):
        if node.right:
            return self._min_node(node.right)
        s = node.parent
        while s and node == s.right:
            node = s
            s = s.parent
        return s
    
    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        
        if v!= None:
            v.parent = u.parent
            

    def delete(self, value):
        z = self.tree_search(value)
        if z == None:
            raise KeyError(f"Key not found: {value}")
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.successor(z)
            if y.parent.value != z.value:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

if __name__ == "__main__":
    t = BST()
    for v in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        t.insert(v)
    
    print("Inorder :", t.inorder())
    t.delete(3)
    print("Inorder after delete 3 : ", t.inorder())
    t.delete(10)
    print("Inorder after delete 10 : ", t.inorder())
