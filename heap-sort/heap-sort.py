import numpy as np


class HeapSort():
    def __init__(self, arr):
        self.arr = [None]
        self.arr += list(arr)
        self.N = len(self.arr) - 1

    def sink(self, k):
        # k = 1
        while 2*k <= self.N:
            j = 2*k
            if j < self.N and self.arr[j] < self.arr[j+1]:
                j += 1
            if self.arr[j] < self.arr[k]:
                break
            else:
                temp = self.arr[j]
                self.arr[j] = self.arr[k]
                self.arr[k] = temp
            k = j

    def sort(self):
        for k in range(self.N//2, 0, -1):
            self.sink(k)
        print('built heap:\n', self.arr)
        while self.N > 1:
            temp = self.arr[self.N]
            self.arr[self.N] = self.arr[1]
            self.arr[1] = temp
            self.N -= 1
            self.sink(1)

    def print_arr(self):
        return self.arr


if __name__ == '__main__':
    arr = np.random.randint(0, 100, 10)
    hs = HeapSort(arr)
    print('original array:\n', hs.print_arr())
    hs.sort()
    print('ordered array:\n', hs.print_arr())
