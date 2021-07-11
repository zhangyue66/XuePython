# for Tree , we need Node(element,lchild,rchild)

class Node(object):
    def __init__(self,item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    def __init__(self):
        self.root = None


    def add(self,item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return

        else:
            queue = [self.root]
            while queue is not None:
                cur_node = queue.pop(0)
                if cur_node.lchild is None:
                    cur_node.lchild = node
                    return
                else:
                    queue.append(cur_node.lchild)
                if cur_node.rchild is None:
                    cur_node.rchild = node
                    return
                else:
                    queue.append(cur_node.rchild)


    def breadth_travel(self):
        if self.root == None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem,end=" ")
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self,node):
        if node == None:
            return
        else:
            print(node.elem,end=" ")
            self.preorder(node.lchild)
            self.preorder(node.rchild)

    def inorder(self,node):
        if node == None:
            return
        else:
            self.inorder(node.lchild)
            print(node.elem,end=" ")
            self.inorder(node.rchild)

    def postorder(self,node):
        if node == None:
            return
        else:
            self.postorder(node.lchild)

            self.postorder(node.rchild)
            print(node.elem, end=" ")


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print("\n")
    tree.preorder(tree.root)
    print("\n")
    tree.inorder(tree.root)
    print("\n")
    tree.postorder(tree.root)
    print("\n")


    tree_two = Tree()
    tree_two.add(1)
    tree_two.add(2)
    tree_two.add(2)
    tree_two.add(None)
    tree_two.add(3)
    tree_two.add(None)
    tree_two.add(3)
    tree_two.inorder(tree_two.root)
    print()