
class ThreeWayQuickSort():
    """This has order of growth O(XXX)"""

    def __init__(self, arr):
        self.arr = arr

    def three_way_quick_sort(self, low, high):
        if low >= high:
            return

        i, lt = low, low
        gt = high-1
        v = self.arr[low]

        while i <= gt:
            if v > self.arr[i]:
                temp = self.arr[i]
                self.arr[i] = self.arr[lt]
                self.arr[lt] = temp
                i += 1
                lt += 1
            elif self.arr[i] > v:
                temp = self.arr[gt]
                self.arr[gt] = self.arr[i]
                self.arr[i] = temp
                gt -= 1
            else:
                i += 1

        self.three_way_quick_sort(low, lt)
        self.three_way_quick_sort(gt+1, high)

    def print_arr(self):
        return self.arr


if __name__ == '__main__':
    # arr = np.random.randint(0, 100, 5)
    arr = ['J', 'A', 'Y', 'E', 'S', 'H', 'S', 'A', 'L', 'V', 'I']
    qs = ThreeWayQuickSort(arr)
    print('original array is:\n', qs.print_arr())
    qs.three_way_quick_sort(0, len(arr))
    print('sorted array is:\n', qs.print_arr())
