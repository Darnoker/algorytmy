import random


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1


class BinaryTree_RB:
    def __init__(self):
        self.root = None

    def add_node(self, key):
        current = self.root
        par = None
        node = Node(key)

        while current is not None:
            par = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right
        node.parent = par
        if par is None:
            self.root = node
        else:
            if node.key < par.key:
                par.left = node
            else:
                par.right = node

        self.fix_insert(node)

    def rotate_left(self, node: Node):
        right_node = node.right
        node.right = right_node.left

        if right_node.left is not None:
            right_node.left.parent = node

        right_node.parent = node.parent
        if node.parent is None:
            self.root = right_node
        elif node == node.parent.left:
            node.parent.left = right_node
        else:
            node.parent.right = right_node
        right_node.left = node
        node.parent = right_node

    def rotate_right(self, node: Node):
        left_node = node.left
        node.left = left_node.right
        if left_node.right != None:
            left_node.right.parent = node

        left_node.parent = node.parent
        if node.parent == None:
            self.root = left_node
        elif node == node.parent.right:
            node.parent.right = left_node
        else:
            node.parent.left = left_node
        left_node.right = node
        node.parent = left_node

    def fix_insert(self, node):
        while node != self.root and node.parent.color == 1:
            if node.parent == node.parent.parent.right:
                uncle = node.parent.parent.left  
                if uncle is not None and uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.rotate_left(node.parent.parent)
            else:
                uncle = node.parent.parent.right 
                if uncle is not None and uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.rotate_right(node.parent.parent)
        self.root.color = 0

    def printTree(self):
        current = self.root
        stack = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.key,current.color, end=" ")
                current = current.right
            else:
                break
        print()
        
    def tree_max_height(self):
        if self.root is None:
            return 0

        q = []

        q.append(self.root)
        height = 0

        while(True):
            nodeCount = len(q)
            if nodeCount == 0:
                return height

            height += 1

            while(nodeCount > 0):
                node = q[0]
                q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

                nodeCount -= 1

    def tree_min_height(self):
        if self.root is None:
            return 0

        q = []

        q.append(self.root)
        height = 0

        while(True):
            nodeCount = len(q)
            if nodeCount == 0:
                return height

            height += 1
            while(nodeCount > 0):
                node = q[0]
                q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                elif node.right is None and node.left is None:
                    return height

                nodeCount -= 1

    def count_red(self):
        if self.root is None:
            return 0
        q = []

        q.append(self.root)
        count = 0

        while(True):
            nodeCount = len(q)
            if nodeCount == 0:
                return count

            while(nodeCount > 0):
                node = q[0]
                if node.color == 1:
                    count += 1
                q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

                nodeCount -= 1


tree = BinaryTree_RB()
tree.add_node(10)
tree.add_node(12)
tree.add_node(15)
tree.add_node(2)
tree.add_node(42)
tree.add_node(12)
tree.add_node(34)
tree.add_node(15)
tree.add_node(43)
tree.printTree()
print("RED:",tree.count_red())
print("max:",tree.tree_max_height())
print("min:", tree.tree_min_height())
print()
print()
print("New Tree:")


new_tree = BinaryTree_RB()

for i in range(10000):
    new_tree.add_node(random.randint(0, 100))

print("RED:",new_tree.count_red())
print("max:",new_tree.tree_max_height())
print("min:", new_tree.tree_min_height())
