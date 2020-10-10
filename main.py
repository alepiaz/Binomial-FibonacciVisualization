from binomialheap import *

bheap = BinomialHeap()

bheap.insert(1)
# bheap.visualizeTree()
bheap.insert(3)
# bheap.visualizeTree()
bheap.insert(5)
# bheap.visualizeTree()
bheap.insert(6)
# bheap.visualizeTree()
bheap.insert(9)
# bheap.visualizeTree()
bheap.insert(2)
# bheap.visualizeTree()
bheap.insert(11)
# bheap.visualizeTree()
bheap.insert(4)

# print(bheap.findNode(11))
# bheap.delete(11)
bheap.delete(3)
# bheap.delete(9)

bheap.visualizeTree()
