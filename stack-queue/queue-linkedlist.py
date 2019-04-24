class Node():

    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList():

    def __init__(self):
        self.head = None
        pass

    def _enqueue(self, node_val):
        if self.head is None:
            self.head = Node(node_val)
        else:
            temp = self.head
            while(temp.next_node is not None):
                temp = temp.next_node
            temp.next_node = Node(node_val)

    def _dequeue(self):
        if self.head:
            first_element = self.head.data
            temp = self.head.next_node
            del self.head
            self.head = temp
            return first_element
        else:
            return None


if __name__ == '__main__':
    ll = LinkedList()
    print('inserting 3,2,4 and 5 in a list')
    ll._enqueue(3)
    ll._enqueue(2)
    ll._enqueue(4)
    ll._enqueue(5)
    print('dequeued element: ', ll._dequeue())
    print('dequeued element: ', ll._dequeue())
    print('dequeued element: ', ll._dequeue())
    print('dequeued element: ', ll._dequeue())
    print('dequeued element: ', ll._dequeue())
