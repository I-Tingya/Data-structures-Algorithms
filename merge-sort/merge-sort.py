import numpy as np


class MergeSort():
    """This has order of growth O(NLogN)"""

    def __init__(self, arr):
        self.arr = arr

    def merge(self, low, mid, high):
        aux_arr = np.zeros(len(self.arr))
        aux_arr[low:high] = self.arr[low:high]
        # print(aux_arr)
        i = low
        mid = mid  # low + (high-low)//2
        j = mid+1
        if low == high:
            return

        for k in range(low, high, 1):

            if i >= mid:
                self.arr[k] = aux_arr[j-1]
                j += 1
            elif j > high:
                self.arr[k] = aux_arr[i]
                i += 1
            elif aux_arr[j-1] < aux_arr[i]:
                self.arr[k] = aux_arr[j-1]
                j += 1
            else:
                self.arr[k] = aux_arr[i]
                i += 1
        # print('array', self.arr)

    def merge_sort(self, low, high):
        # print('printing low/high', low, high)
        if high == low+1:
            return
        mid = low + (high-low)//2
        self.merge_sort(low, mid)
        # print('moving to second half')
        # print('printing mid/high', mid, high)
        self.merge_sort(mid, high)
        # print('printing low/mid/high', low, mid, high)
        self.merge(low, mid, high)

    def print_arr(self):
        return self.arr


if __name__ == '__main__':
    arr = np.array(np.random.randint(0, 100, 10))
    ms = MergeSort(arr)
    print('original array is:\n', ms.print_arr())
    ms.merge_sort(0, len(arr))
    print('sorted array is:\n', ms.print_arr())
