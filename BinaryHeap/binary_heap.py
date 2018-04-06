from enum import Enum

class HeapType(Enum):
    MIN_HEAP = 1
    MAX_HEAP = 2


class BinaryHeap:

    # default is min heap.
    def __init__(self, type=HeapType.MIN_HEAP):
        self.type = type
        self.__size = 0
        self.__heap = [0]

    def create_binary_heap(self,l):
        for e in l:
            # print "inserting  "+str(e)
            self.insert(e)

    def insert(self, val=None):
        if val is None:
            raise ValueError("Trying to insert invalid value to the heap.")
        else:
            self.__size += 1
            self.__heap.append(val)
            self.adjust_up()

            # print "heap : ",
            # print self.__heap
            # print

    def adjust_up(self):
        i = self.__size
        # print "size: " + str(i)
        while i/2 > 0:
            if self.type == HeapType.MIN_HEAP:
                if self.__heap[i] < self.__heap[i/2]:
                    self.__heap[i],self.__heap[i/2] = self.__heap[i/2],self.__heap[i]
            elif self.type == HeapType.MAX_HEAP:
                if self.__heap[i] > self.__heap[i/2]:
                    self.__heap[i],self.__heap[i/2] = self.__heap[i/2],self.__heap[i]
            i = i/2

    def get_min_child(self,i):
        if 2*i + 1 > self.__size:
            return 2*i
        else:
            # print "i: " + str(i)
            # print "size: "+ str(self.__size)

            if self.__heap[2*i] <= self.__heap[2*i + 1]:
                return 2*i
            else:
                return 2*i+1

    def get_max_child(self,i):
        if 2*i+1 > self.__size:
            return 2*i
        else:
            if self.__heap[2*i] > self.__heap[2*i + 1]:
                return 2*i
            else:
                return 2*i+1

    def adjust_down(self):
        i = 1
        while 2*i <= self.__size:
            # print "in adjust_down"
            if self.type == HeapType.MIN_HEAP:
                min_child_index = self.get_min_child(i)
                # print "min_child_index:" + str(min_child_index)
                # print "swap"
                if self.__heap[min_child_index] < self.__heap[i]:
                    self.__heap[i],self.__heap[min_child_index] = self.__heap[min_child_index],self.__heap[i]
                i = min_child_index
            elif self.type == HeapType.MAX_HEAP:
                max_child_index = self.get_max_child(i)
                if self.__heap[max_child_index] > self.__heap[i]:
                    self.__heap[i],self.__heap[max_child_index] = self.__heap[max_child_index],self.__heap[i]
                i = max_child_index

    #removes the top from heap.
    def remove(self):
        if self.__size > 1:
            e = self.__heap[1]
            # print "removed element: " + str(e)
            # move last element to the top the heap
            self.__heap[1] = self.__heap[self.__size]
            self.__heap.pop()
            self.__size -= 1
            self.adjust_down()

            # print "removed " + str(e)
            # print "size:" + str(self.__size)
            # print "heap: ",
            # print self.__heap
            return e
        elif self.__size == 1:
            e = self.__heap[1]
            self.__size -= 1
            return e
        else:
            raise ValueError("Trying to remove when heap is empty")

    # looks at the root of the heap and returns its value but doesn't remove the root
    def peek(self):
        if self.__size >= 1:
            return self.__heap[1]
        else:
            raise ValueError("Heap is empty, can't peek")

    def print_heap(self):
        print "printing the heap in order:"
        while self.__size >= 1:
            e = self.remove()
            print str(e) + ",",
        print

    def get_size(self):
        return self.__size

    def get_heap(self):
        return self.__heap

if __name__ == "__main__":
    l = [5,18,27,14,9,33,21,19,17,11,7]
    # l = [19,21,33,27]
    min_heap = BinaryHeap(HeapType.MIN_HEAP)
    min_root = min_heap.create_binary_heap(l)
    print "min heap size : " + str(min_heap.get_size())
    print "Internal min heap array: "
    print min_heap.get_heap()


    min_heap.print_heap()

    max_heap = BinaryHeap(HeapType.MAX_HEAP)
    max_root = max_heap.create_binary_heap(l)
    print "max heap size : " + str(max_heap.get_size())
    print "Internal max heap array: "
    print max_heap.get_heap()
    max_heap.print_heap()