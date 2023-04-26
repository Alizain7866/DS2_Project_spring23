import sys 
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1
        
class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        self.root = self._insert_helper(self.root, key)
    
    def _insert_helper(self, node, key):
        if node is None:
            return Node(key)
        elif key < node.key:
            node.left = self._insert_helper(node.left, key)
        else:
            node.right = self._insert_helper(node.right, key)
            
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        
        balance_factor = self._get_balance_factor(node)
        
        if balance_factor > 1 and key < node.left.key:
            return self._right_rotate(node)
        elif balance_factor < -1 and key > node.right.key:
            return self._left_rotate(node)
        elif balance_factor > 1 and key > node.left.key:
            if node.left is not None:
                node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        elif balance_factor < -1 and key < node.right.key:
            if node.right is not None:
                node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        
        return node
    
    def delete(self, key):
        if not self.root:
            return self.root

        def _delete(root, key):
            if not root:
                return root

            elif key < root.key:
                root.left = _delete(root.left, key)

            elif key > root.key:
                root.right = _delete(root.right, key)

            else:
                # node with only one child or no child
                if not root.left:
                    temp = root.right
                    root = None
                    return temp

                elif not root.right:
                    temp = root.left
                    root = None
                    return temp

                # node with two children
                temp = self.minValueNode(root.right)
                root.key = temp.key
                root.right = _delete(root.right, temp.key)

            if not root:
                return root

            # update height of the current node
            root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

            # get the balance factor of the node
            balance = self.getBalance(root)

            # if the node is unbalanced, try out the 4 cases
            if balance > 1 and self.getBalance(root.left) >= 0:
                return self.rightRotate(root)

            if balance < -1 and self.getBalance(root.right) <= 0:
                return self.leftRotate(root)

            if balance > 1 and self.getBalance(root.left) < 0:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

            if balance < -1 and self.getBalance(root.right) > 0:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

            return root

        return _delete(self.root, key)

    def minValueNode(self, node):
            current = node
            while current.left is not None:
                current = current.left
            return current

        
    def _left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))
        
        return new_root
    
    def _right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))
        
        return new_root
        
    def _get_height(self, node):
        if node is None:
            return 0
        else:
            return node.height
        
    def _get_balance_factor(self, node):
        if node is None:
            return 0
        else:
            return self._get_height(node.left) - self._get_height(node.right)
    
    def search(self, key):
        return self._search_helper(self.root, key)
    
    def _search_helper(self, node, key):
        if node is None:
            return False
        elif node.key == key:
            return True
        elif key < node.key:
            return self._search_helper(node.left, key)
        else:
            return self._search_helper(node.right, key)

        
    def space_complexity(self):
        if not self.root:
            return 0
        
        stack = [self.root]
        size = 1
        
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                size += 1
            if node.right:
                stack.append(node.right)
                size += 1
        
        return size * sys.getsizeof(Node(None))

