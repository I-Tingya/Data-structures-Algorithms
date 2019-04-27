import numpy as np


class QuickSelect():
    """This has order of growth O(XXX)"""

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

    def quick_select(self, low, high, kth):
        while high > low:
            # print(low, high)
            j = self.partition(low, high)
            if j > kth:
                high = j-1
            if j < kth:
                low = j+1
            else:
                return self.arr[kth]
        return self.arr[kth]

    def print_arr(self):
        return self.arr


if __name__ == '__main__':
    arr = np.random.randint(0, 100, 5)
    qs = QuickSelect(arr)
    print('given array is:\n', qs.print_arr())
    print('kth largest number', qs.quick_select(0, len(arr), 3))
