import numpy as np


class QuickSort():
    """This has order of growth O(NLogN)"""

    def __init__(self, arr):
        self.arr = arr

    def partition(self, low, high):
        i = low
        j = high - 1
        k = low
        while True:

            while self.arr[i] < self.arr[k]:
                i += 1
                if i >= high-1:
                    break
            while self.arr[k] < self.arr[j]:
                j -= 1
                if j <= low:
                    break
            if j <= i:
                break

            temp = self.arr[i]
            self.arr[i] = self.arr[j]
            self.arr[j] = temp
        temp = self.arr[j]
        self.arr[j] = self.arr[k]
        self.arr[k] = temp
        return j

    def quick_sort(self, low, high):
        if low >= high:
            return
        j = self.partition(low, high)
        self.quick_sort(low, j-1)
        self.quick_sort(j+1, high)

    def print_arr(self):
        return self.arr


if __name__ == '__main__':
    arr = np.random.randint(0, 100, 10)
    qs = QuickSort(arr)
    print('original array is:\n', qs.print_arr())
    qs.quick_sort(0, len(arr))
    print('sorted array is:\n', qs.print_arr())
