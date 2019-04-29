class Node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


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

    def put(self, key, val):
        if self.root is None:
            self.root = Node(key, val)
        else:
            x = self.root
            while x is not None:
                if key > x.key:
                    p = x
                    x = x.right
                elif key < x.key:
                    p = x
                    x = x.left
                else:
                    x.val = val
            if p.key < key:
                p.right = Node(key, val)
            else:
                p.left = Node(key, val)

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


if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.put('Jayesh', 10)
    bst.put('Umang', 20)
    bst.put('Vaibhav', 30)
    bst.put('Omkar', 40)
    bst.print_symbol_table()
    print('Omkar\'s score is: ', bst.get('Omkar'))
    print('Minimum key is: ', bst.find_min())
    print('Maximum key is: ', bst.find_max())
