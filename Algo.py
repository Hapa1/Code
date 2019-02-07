class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# create nodes
root = Node('A')
n1 = Node('B')
n2 = Node('C')
n3 = Node('D')
n4 = Node('E')

# setup children
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4

def level_order(root):
    if root is None:
        return
    q = []
    q.append(root)
