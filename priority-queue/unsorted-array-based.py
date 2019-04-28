class UnsortedArrayPQ():
    def __init__(self):
        self.arr = []

    def insert(self, val):
        self.arr.append(val)

    def max_delete(self):
        max_ = 0
        for i in range(len(self.arr)):
            if self.arr[i] > self.arr[max_]:
                max_ = i
        temp = self.arr[max_]
        self.arr[max_] = self.arr[-1]
        del self.arr[-1]
        return temp

    def print_arr(self):
        print(self.arr)


if __name__ == '__main__':
    bh = UnsortedArrayPQ()
    bh.insert(11)
    bh.insert(33)
    bh.insert(29)
    bh.insert(72)
    bh.insert(8)
    bh.print_arr()
    print('deleting max element:', bh.max_delete())
    bh.print_arr()
    bh.insert(60)
    bh.print_arr()
    print('deleting max element:', bh.max_delete())
    bh.print_arr()
