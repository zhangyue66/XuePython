class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object,):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        if self.root and self.root.left == None and self.root.right == None:
            if new_val < self.root.value:
                self.root.left = Node(new_val)
            else:
                self.root.right = Node(new_val)
        elif self.root.left.value > new_val:
            self.root.left.left = Node(new_val)
        elif self.root.left.value < new_val:
            self.root.left.right = Node(new_val)

        return 1

    def search(self, find_val):
        return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

#print(tree.root.left.left.value)
# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
