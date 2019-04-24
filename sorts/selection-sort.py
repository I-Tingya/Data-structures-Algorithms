import numpy as np


class Selection():

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        for i in range(len(self.arr)):
            min_idx = i
            for j in range(i+1, len(self.arr)):
                if self.arr[j] < self.arr[min_idx]:
                    min_idx = j
            # swap min index with start pointer i.e. i
            temp = self.arr[i]
            self.arr[i] = self.arr[min_idx]
            self.arr[min_idx] = temp

    def print_arr(self):
        return self.arr


if __name__ == '__main__':
    arr = Selection(np.array([5, 6, 4, 2, 7, 1]))
    print('printing original array: ', arr.print_arr())
    arr.sort()
    print('printing sorted array: ', arr.print_arr())
