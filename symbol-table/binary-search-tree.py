class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.count = 1


class BinarySearchTree():
    def __init__(self):
        self.root = None

    def get(self, key):
        if self.root is None:
            return None
        else:
            x = self.root
            while(x is not None):
                if key < x.key:
                    x = x.left
                if key > x.key:
                    x = x.right
                else:
                    return x.val
            return None

    def put_node(self, key, val):
        self.root = self.put(self.root, key, val)

    def put(self, node, key, val):
        if node is None:
            return Node(key, val)
        if key > node.key:
            node.right = self.put(node.right, key, val)
        if key < node.key:
            node.left = self.put(node.left, key, val)
        node.count = 1 + self.size(node.right) + self.size(node.left)
        return node

    def find_min(self):
        x = self.root
        min_ = x.key
        x = x.left
        while x is not None:
            if x.key < min_:
                min_ = x.key
                x = x.left
        return min_

    def find_max(self):
        x = self.root
        max_ = x.key
        x = x.right
        while x is not None:
            if x.key > max_:
                max_ = x.key
                x = x.right
        return max_

    def find_floor(self, key):
        x = self.floor_(self.root, key)
        if x is None:
            return None
        else:
            return x.key

    def floor_(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self.floor_(node.left, key)
        x = self.floor_(node.right, key)
        if x is not None:
            return x
        else:
            return node

    def find_ceil(self, key):
        x = self.ceil_(self.root, key)
        if x is None:
            return None
        else:
            return x.key

    def ceil_(self, node, key):
        if node is None:
            return None
        if node.key == key:
            return node
        if key > node.key:
            return self.ceil_(node.right, key)
        x = self.ceil_(node.left, key)
        if x is not None:
            return x
        else:
            return node

    def size(self, node):
        if node is None:
            return 0
        else:
            return node.count

    def print_size(self):
        return self.root.count

    def print_rank(self, key):
        return self.rank(self.root, key)

    def rank(self, node, key):
        if node is None:
            return 0
        if key < node.key:
            return self.rank(node.left, key)
        elif key > node.key:
            return 1 + self.size(node.left) + self.rank(node.right, key)
        else:
            return self.size(node.left)

    def print_symbol_table(self, node=None):
        if node is None:
            node = self.root
            print('printing head first\n', node.key, node.val)
        else:
            print(node.key, node.val)
        if node.left is not None:
            self.print_symbol_table(node=node.left)
        if node.right is not None:
            self.print_symbol_table(node=node.right)

    def print_keys(self):
        self.key_arr = []
        self.inorder(self.root)
        return self.key_arr

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        self.key_arr.append(node.key)
        self.inorder(node.right)


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.put_node('Jayesh', 10)
    bst.put_node('Umang', 20)
    bst.put_node('Vaibhav', 30)
    bst.put_node('Omkar', 40)
    bst.put_node('Bakulesh', 40)
    bst.print_symbol_table()
    print('printing keys:\n', bst.print_keys())
    print('Size of tree is:', bst.print_size())
    print('Rank of key Omkar is:', bst.print_rank('Omkar'))
    print('Rank of key Pratik is:', bst.print_rank('Pratik'))
    print('Omkar\'s score is:', bst.get('Omkar'))
    print('Minimum key is:', bst.find_min())
    print('Maximum key is:', bst.find_max())
    print('Finding floor key for P:', bst.find_floor('P'))
    print('Finding floor key for K:', bst.find_floor('K'))
    print('Finding ceil key for A:', bst.find_ceil('A'))
    print('Finding ceil key for R:', bst.find_ceil('R'))
