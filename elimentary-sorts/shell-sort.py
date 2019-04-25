import numpy as np


class Shell():

    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        h = 1
        while(h < len(self.arr)//3):
            h = 3*h + 1  # 1, 4, 13, 40

        while(h >= 1):
            for i in range(h, len(self.arr)):
                for j in range(i, h-1, -h):
                    # print(j, end=' ')
                    if self.arr[j] < self.arr[j-h]:
                        temp = self.arr[j-h]
                        self.arr[j-h] = self.arr[j]
                        self.arr[j] = temp
                # print()

            h = h//3

    def print_arr(self):
        return self.arr


if __name__ == '__main__':
    arr = Shell(np.array([5, 6, 4, 2, 7, 1, 2]))
    print('printing original array: ', arr.print_arr())
    arr.sort()
    print('printing sorted array: ', arr.print_arr())
