# Node for Binary Search Tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None   # smaller to the left
        self.right = None  # greater to the right


# simple BST: insert, contains (search), delete, Min/Max, Predecessor/Successor, Traversals
class BST:
    def __init__(self):
        self.root = None

    # --- Insert ---
    def insert(self, value):
       if self.root == None:
           self.root=Node(value)
       else:
           self._insert(self.root, value)
       
    def _insert(self, node, value):
        if value<node.value:
            if node.left:
                self._insert(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._insert(node.right, value)
            else:
                node.right = Node(value)
               

    # --- Contains / Search ---
    def contains(self, value):
        return self._contains(self.root, value)
    
    def _contains(self, node, value):
        if node.value == value:
            return True
        elif node is None:
            return False
        elif node.value > value:
            return self._contains(node.left, value)
        elif node.value < value:
            return self._contains(node.right, value)


    # --- Min / Max ---
    def min(self):
        current = self.root
        while current.left:
            current = current.left
        return current.value


    def max(self):
        current = self.root
        while current.right:
            current = current.right
        return current.value

    # --- Predecessor / Successor ---
    def successor(self, value):
        node = self.root
        succ = None
        while node:
            if value < node.value:
                succ = node
                node = node.left
            elif value > node.value:
                node = node.right
            else: 
                if node.right:
                    succ = self._min_node(node.right)
                break
        return succ.value if succ else None

    
    def predecessor(self, value):
        node = self.root
        pred = None
        while node:
            if value > node.value:
                pred = node
                node = node.right
            elif value < node.value:
                node = node.left
            else:
                if node.left:
                    pred = node.left
                    while pred.right:
                        pred = pred.right
                break
        return pred.value if pred else None

    # --- Delete ---
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            raise KeyError(f"Key not found: {value}")
        
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            successor = self._min_node(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
        return node

    def _min_node(self, node): #leftest of the subtree
        min = node
        while min and min.left:
            min = min.left
        return min
    
    # --- Traversals ---
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result
    
    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)


    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result
    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)



# --- test your implementation ---
if __name__ == "__main__":
    t = BST()
    for v in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
        t.insert(v)

    print("Inorder  :", t.inorder())   # Inorder Traversal should deliver ordered sequence
    print("Contains 7?", t.contains(7))  # should return true
    print("Min/Max  :", t.min(), t.max())  # should return 1 14
    print("Predecessor/Successor  :", t.predecessor(t.root.value), t.successor(t.root.value))  # 7 10

    t.delete(3)   # deletes a node with 2 children (3 -> successor 4)
    print("Inorder  :", t.inorder())

    t.delete(10)  # deletes a node with 1 child
    print("Inorder  :", t.inorder())

    #t.delete(99)  # should deliver an error, Key not found
