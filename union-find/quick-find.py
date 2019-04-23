import numpy as np
import sys


class QuickFind():
    """This class implements QuickFind implementation of UnionFind algorithm
        Here cost of Find is 1 against N for union.
        Order of growth is O(N^2) """

    # _node_arr = None
    # _no_of_nodes = 0

    def __init__(self, no_of_nodes):
        self._no_of_nodes = no_of_nodes
        self._node_arr = np.arange(self._no_of_nodes)

    def _connected(self, node_1, node_2) -> bool:
        if self._node_arr[node_1] == self._node_arr[node_2]:
            print('Given nodes are connected')
            return True
        else:
            print('Given nodes are not connected')
            return False

    def _union(self, node_1, node_2):
        if self._connected(node_1, node_2):
            print('Given nodes are connected')
            pass
        else:
            print('connecting given nodes and the connected components')
            id_node_1 = self._node_arr[node_1]
            id_node_2 = self._node_arr[node_2]
            for idx in range(self._no_of_nodes):
                if self._node_arr[idx] == id_node_2:
                    self._node_arr[idx] = id_node_1


if __name__ == '__main__':
    no_of_nodes = int(sys.argv[1])
    qf = QuickFind(no_of_nodes)

    while(True):
        # user input can be connected 2 3 or union 2 3 or stop
        user_input = input(
            'enter operation(connected/union) and nodes:\n'
                ).split()
        if user_input[0] == 'connected':
            qf._connected(int(user_input[1]), int(user_input[2]))
        if user_input[0] == 'union':
            qf._union(int(user_input[1]), int(user_input[2]))
        if user_input[0] == 'stop':
            break
