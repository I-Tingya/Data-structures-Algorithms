import numpy as np
import sys


class QuickUnionPathCompression():
    """This class implements QuickUnion implementation of UnionFind algorithms
        Here cost of find is N and cost of union us also N in worst case.
        Order of growth is O(NlogN) """

    # _node_arr = None
    # _no_of_nodes = 0

    def __init__(self, no_of_nodes):
        self._no_of_nodes = no_of_nodes
        self._node_arr = np.arange(self._no_of_nodes)

    def _root(self, node_x):
        idx = node_x
        while(self._node_arr[idx] != idx):
            # The only difference wrt quick union is below one line
            self._node_arr[idx] = self._node_arr[self._node_arr[idx]]
            idx = self._node_arr[idx]
        return idx

    def _connected(self, node_1, node_2):
        if self._root(node_1) == self._root(node_2):
            print('nodes are connected')
        else:
            print('nodes are not connected')

    def _union(self, node_1, node_2):
        print('connecting given nodes if not connected')
        self._node_arr[self._root(node_1)] = self._root(node_2)


if __name__ == '__main__':
    no_of_nodes = int(sys.argv[1])
    qupc = QuickUnionPathCompression(no_of_nodes)

    while(True):
        user_input = input(
            'Enter operation(connected/union) and nodes:\n'
            ).split()

        if user_input[0] == 'connected':
            qupc._connected(int(user_input[1]), int(user_input[2]))
        if user_input[0] == 'union':
            qupc._union(int(user_input[1]), int(user_input[2]))
        if user_input[0] == 'stop':
            break
