class BinaryHeap():
    def __init__(self):
        self.arr = [None]
        self.N = 0

    def insert(self, val):
        self.N += 1
        self.arr.append(val)
        self.swim()

    def max_del(self):
        max_ = self.arr[1]
        self.arr[1] = self.arr[self.N]
        self.sink()
        del self.arr[self.N]
        self.N -= 1
        return max_

    def swim(self):
        k = self.N
        while k > 1 and (self.arr[k//2] < self.arr[k]):
            temp = self.arr[k]
            self.arr[k] = self.arr[k//2]
            self.arr[k//2] = temp
            k = k//2

    def sink(self):
        k = 1
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

    def print_arr(self):
        print(self.arr)


if __name__ == '__main__':
    bh = BinaryHeap()
    bh.insert(11)
    bh.insert(33)
    bh.insert(29)
    bh.insert(72)
    bh.insert(8)
    bh.print_arr()
    print('deleting max element:', bh.max_del())
    bh.print_arr()
    bh.insert(60)
    bh.print_arr()
    print('deleting max element:', bh.max_del())
    bh.print_arr()
