import numpy as np


class Insertion():

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(len(self.arr)):
            for j in range(i, 0, -1):
                if self.arr[j] < self.arr[j-1]:
                    temp = self.arr[j-1]
                    self.arr[j-1] = self.arr[j]
                    self.arr[j] = temp

    def print_arr(self):
        return self.arr


if __name__ == '__main__':
    arr = Insertion(np.array([5, 6, 4, 2, 7, 1, 2]))
    print('printing original array: ', arr.print_arr())
    arr.sort()
    print('printing sorted array: ', arr.print_arr())
