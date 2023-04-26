import random

class SkipNode:
    def __init__(self, val=None, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down

class SkipList:
    def __init__(self):
        self.head = SkipNode()
    
    def search(self, target):
        curr = self.head
        while curr:
            if curr.right and curr.right.val <= target:
                curr = curr.right
            elif curr.val == target:
                return True
            else:
                curr = curr.down
        return False
    
    def insert(self, val):
        node = SkipNode(val)
        curr = self.head
        nodes_to_update = []
        while curr:
            if curr.right and curr.right.val < val:
                curr = curr.right
            else:
                nodes_to_update.append(curr)
                curr = curr.down
        for i in range(len(nodes_to_update)):
            node.right = nodes_to_update[i].right
            nodes_to_update[i].right = node
            if i > 0:
                nodes_to_update[i-1].down = node
            if random.random() < 0.5:
                break

    def remove(self, val):
        curr = self.head
        found = False
        while curr:
            if curr.right and curr.right.val < val:
                curr = curr.right
            elif curr.right and curr.right.val == val:
                found = True
                curr.right = curr.right.right
                curr = curr.down
            else:
                curr = curr.down
        return found
