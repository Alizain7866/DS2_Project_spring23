import sys 
from typing import Tuple, List
class Node:
    def __init__(self, key: int, value: List):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1
        self.value = value
        
class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key: int, value: List):
        self.root = self._insert_helper(self.root, key, value)
    
    def _insert_helper(self, node: Node, key: int, value: List):
        if node is None:
            node = Node(key, value)
        elif key < node.key:
            node.left = self._insert_helper(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_helper(node.right, key, value)
        else:
            node.value.append(key)
            return node
        
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

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if not node:
            return None
        elif key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            # Case 1: No children
            if not node.left and not node.right:
                node = None
            # Case 2: One child
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            # Case 3: Two children
            else:
                # Find the smallest key in the right subtree
                temp = self._find_min(node.right)
                node.key = temp.key
                node.right = self._remove(node.right, temp.key)

        if not node:
            return None

        # Update the height of the current node
        node.height = 1 + max(self._get_height(node.left),
                              self._get_height(node.right))

        # Check if the node is balanced
        balance = self._get_balance_factor(node)

        # Left-Left Case
        if balance > 1 and self._get_balance_factor(node.left) >= 0:
            return self._right_rotate(node)

        # Right-Right Case
        if balance < -1 and self._get_balance_factor(node.right) <= 0:
            return self._left_rotate(node)

        # Left-Right Case
        if balance > 1 and self._get_balance_factor(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right-Left Case
        if balance < -1 and self._get_balance_factor(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node
    
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node        
    
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

