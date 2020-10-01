from heapq import heapify, heappop, heappush

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self,key):
        heappush(self.heap, key)

    def extractMin(self):
        return heappop(self.heap)

    def getParent(self, i):
        return int((i-1)/2)

    def decreaseKey(self,i,x):
        if x < i:
            self.heap[i] = x
            while i and self.heap[self.getParent(i)] > self.heap[i]:
                self.heap[i], self.heap[self.getParent(i)] = (self.heap[self.getParent(i)], self.heap[i])
        else:
            print("Value must be smaller in order to call decreaseKey function")

    def delete(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    def getMin(self):
        return self.heap[0]

heap = MinHeap()

heap.insert(3)
heap.insert(2)
heap.insert(4)
heap.insert(8)
heap.insert(0)

print(heap.extractMin())
print(heap.getMin())
print(heap.heap)
