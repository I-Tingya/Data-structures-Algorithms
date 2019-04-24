class Node():

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList():

    def __init__(self):
        self.head = None
        pass

    def _push(self, node_val):
        if self.head is None:
            self.head = Node(node_val)
        else:
            temp = self.head
            while(temp.next_node is not None):
                temp = temp.next_node
            temp.next_node = Node(node_val)

    def _pop(self):
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


if __name__ == '__main__':
    ll = LinkedList()
    print('inserting 3,2,4 and 5 in a list')
    ll._push(3)
    ll._push(2)
    ll._push(4)
    ll._push(5)
    print('popped element is: ', ll._pop())
    print('popped element is: ', ll._pop())
    print('popped element is: ', ll._pop())
    print('popped element is: ', ll._pop())
    print('popped element is: ', ll._pop())
