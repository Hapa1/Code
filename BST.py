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
    r = []
    q.append(root)

    while(len(q) > 0):
        print(q[0].data)
        t = []
        node = q.pop(0)
        if node.left is not None:
            t.append(node.left.data)
            q.append(node.left)
        if node.right is not None:
            t.append(node.right.data)
            q.append(node.right)
        r.append(t)
    print(r)
level_order(root)

