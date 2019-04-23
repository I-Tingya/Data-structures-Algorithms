import numpy as np
import sys


class WeightedQuickUnionPathCompression():
    """This class implements weighted quick union implementation of
        UnionFind algorithm.
        Cost of find and union here is logN (i.e. depth=3 for 8 nodes)
        Order of growth is O(Nlog*N) """

    # _no_of_nodes = 0
    # _node_arr = None
    # _size_arr = None

    def __init__(self, no_of_nodes):
        self._no_of_nodes = no_of_nodes
        self._node_arr = np.arange(self._no_of_nodes)
        self._size_arr = np.ones(self._no_of_nodes)

    def _root(self, node_x) -> int:
        idx = node_x
        while(idx != self._node_arr[idx]):
            self._node_arr[idx] = self._node_arr[self._node_arr[idx]]
            idx = self._node_arr[idx]
        return idx

    def _connected(self, node_1, node_2):
        if self._root(node_1) == self._root(node_2):
            print('nodes are connected')
        else:
            print('nodes are not connected')

    def _union(self, node_1, node_2):
        root_node_1 = self._root(node_1)
        root_node_2 = self._root(node_2)
        print('connecting nodes')
        if self._size_arr[root_node_1] > self._size_arr[root_node_2]:
            self._node_arr[root_node_2] = root_node_1
            self._size_arr[root_node_1] += self._size_arr[root_node_2]
        elif self._size_arr[root_node_1] < self._size_arr[root_node_2]:
            self._node_arr[root_node_1] = root_node_2
            self._size_arr[root_node_2] += self._size_arr[root_node_1]
        else:
            self._node_arr[root_node_1] = root_node_2
            self._size_arr[root_node_2] += self._size_arr[root_node_1]


if __name__ == '__main__':
    no_of_nodes = int(sys.argv[1])
    wqupc = WeightedQuickUnionPathCompression(no_of_nodes)

    while(True):
        user_input = input(
            'Enter operation(connected/union) and nodes:\n'
            ).split()

        if user_input[0] == 'connected':
            wqupc._connected(int(user_input[1]), int(user_input[2]))
        if user_input[0] == 'union':
            wqupc._union(int(user_input[1]), int(user_input[2]))
        if user_input[0] == 'stop':
            break
