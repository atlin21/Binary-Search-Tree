class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
class BST:
    def __init__(self):
        self.root = None
    def push(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.push2(data, self.root)
    def push2(self, data, current):
        if data < current.data:
            if current.left_child is None:
                current.left_child = Node(data)
            else:
                self.push2(data, current.left_child)
        elif data > current.data:
            if current.right_child is None:
                current.right_child = Node(data)
            else:
                self.push2(data, current.right_child)
        else:
            print("value is already in tree")

    def peek(self):
        if self.root != None:
            self.peek2(self.root)
    def peek2(self, current):
        if current != None:
            self.peek2(current.left_child)
            print(current.data)
            self.peek2(current.right_child)


bst = BST()
bst.push(12)
bst.push(12)
bst.push(13)
bst.push(2)
bst.push(1)
bst.push(24)
bst.peek()