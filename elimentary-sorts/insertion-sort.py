import numpy as np


class Insertion():

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(len(self.arr)):
            next_idx = i
            for j in range(i):
                if self.arr[next_idx] < self.arr[j]:
                    temp = self.arr[next_idx]
                    self.arr[j+1:next_idx+1] = self.arr[j:next_idx]
                    self.arr[j] = temp

    def print_arr(self):
        return self.arr


if __name__ == '__main__':
    arr = Insertion(np.array([5, 6, 4, 2, 7, 1, 2]))
    print('printing original array: ', arr.print_arr())
    arr.sort()
    print('printing sorted array: ', arr.print_arr())
