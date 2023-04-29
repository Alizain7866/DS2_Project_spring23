import random

class Node:
    def __init__(self, val=None, height=1):
        # Each node has a value and a list of pointers to the next nodes at each level
        self.val = val
        self.next = [None] * height
        
class SkipList:
    def __init__(self):
        # The skip list has a head node with no value and a default height of 1
        self.head = Node()
        self.max_height = 1
        
    def random_height(self):
        # Generates a random height for a new node
        height = 1
        while random.random() < 0.5 and height < self.max_height + 1:
            height += 1
        return height
        
    def search(self, target):
        # Searches for a target value in the list, starting at the top and working downwards
        curr = self.head
        for i in range(self.max_height - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        # Returns True if the target is found, False otherwise
        return curr.next[0] and curr.next[0].val == target
        
    def insert(self, val):
        # Inserts a new node with the specified value into the list
        height = self.random_height()
        node = Node(val, height)
        # Ensures the head node has enough pointers for the new node at each level
        while len(self.head.next) < height:
            self.head.next.append(None)
        curr = self.head
        for i in range(self.max_height - 1, -1, -1):
            # Finds the correct position to insert the new node at each level
            while curr.next[i] and curr.next[i].val < val:
                curr = curr.next[i]
            if i < height:
                # Updates the pointers of the new node and the nodes before and after it at each level
                node.next[i] = curr.next[i]
                curr.next[i] = node
        # Updates the maximum height of the list if necessary
        self.max_height = max(self.max_height, height)
        
    def remove(self, val):
        # Removes a node with the specified value from the list
        curr = self.head
        removed = False
        for i in range(self.max_height - 1, -1, -1):
            # Finds the node to remove and updates the pointers of the nodes before and after it at each level
            while curr.next[i] and curr.next[i].val < val:
                curr = curr.next[i]
            if curr.next[i] and curr.next[i].val == val:
                curr.next[i] = curr.next[i].next[i]
                removed = True
        if removed and len(self.head.next) > 1:
            # Updates the maximum height of the list if necessary
            while len(self.head.next) > 1 and not self.head.next[-1]:
                self.head.next.pop()
            self.max_height = len(self.head.next)
