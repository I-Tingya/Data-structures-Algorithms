class Node():

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList():

    def __init__(self):
        self.head = None
        pass

    def _insert(self, node_val):
        if self.head is None:
            self.head = Node(node_val)
        else:
            temp = self.head
            while(temp.next_node is not None):
                temp = temp.next_node
            temp.next_node = Node(node_val)

    def _remove_last(self):
        if self.head.next_node:
            temp = self.head
            while(temp.next_node):
                prev = temp
                temp = temp.next_node
            last_element = temp.data
            prev.next_node = None
            del temp
            return last_element
        elif self.head.next_node is None:
            last_element = self.head.data
            self.head.data = None
            return last_element

    def _remove_first(self):
        if self.head:
            temp = self.head.next_node
            self.head = temp

    def _find_min(self) -> int:
        if self.head:
            min_node = self.head
            temp = self.head
            while(temp.next_node):
                if temp.data < min_node.data:
                    min_node = temp
                temp = temp.next_node
        return min_node.data

    def _find_max(self) -> int:
        if self.head:
            max_node = self.head
            temp = self.head
            while(temp):
                if temp.data > max_node.data:
                    max_node = temp
                temp = temp.next_node
        return max_node.data

    def _print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next_node


if __name__ == '__main__':
    ll = LinkedList()
    print('inserting 2,3,4 and 5 in a list')
    ll._insert(3)
    ll._insert(2)
    ll._insert(4)
    ll._insert(5)
    print('\nprinting original list')
    ll._print_list()
    print('\nminimum value in the list is: ', ll._find_min())
    print('maximum value in the list is: ', ll._find_max())
    print('removed last element: ', ll._remove_last())
    print('list after removing last element')
    ll._print_list()
    ll._remove_first()
    print('\nlist after removing first element')
    ll._print_list()
