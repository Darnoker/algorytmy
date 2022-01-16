from msilib.schema import Binary


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.count = 0

class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, node: Node):
        root = self.root
        par = None

        while root is not None:
            par = root
            if node.key < root.key:
                root = root.left
            else:
                root=root.right

        node.parent = par
        if par is None:
            self.root = node
        else:
            if node.key < par.key:
                par.left = node
                node.count += 1
            else:
                par.right = node
                node.count += 1 
    
    def search_node(self, key: int):
        node = self.root
        while node is not None and node.key != key:
            if key < node.key:
                node=node.left
            else:
                node=node.right

        return node

    def minimum(x):
        while x.left is not None:
            x = x.left
        return x

    def transplant(self,u, v):
        if u.parent is None:
            self.root = v
        else:
            if u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def delete(self, z):
        if z.left is None:
            self.transplant(z, z.right)
        else:
            if z.right is None:
                self.transplant(z, z.left)
            else:
                y=self.minimum(z.right)
                if y.parent is not z:
                    self.transplant(y, y.right)
                    y.right = z.right
                    y.right.parent = y
                self.transplant(z,y)
                y.left = z.left
                y.left.parent = y
                




            


tree = BinaryTree()

tree.add_node(Node(4))

print(tree.root.key)

tree.add_node(Node(4))
