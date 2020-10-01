from binomialheap import *

bheap = BinomialHeap()

bheap.insert(1)
bheap.visualizeTree()
bheap.insert(3)
bheap.visualizeTree()
bheap.insert(5)
bheap.visualizeTree()
bheap.insert(6)
bheap.visualizeTree()
bheap.insert(9)
bheap.visualizeTree()
bheap.insert(2)
bheap.visualizeTree()
bheap.insert(11)
bheap.visualizeTree()
bheap.insert(4)
bheap.visualizeTree()

# print(type(bheap.visualizeTree()))


# print(bheap.findNode(1))
# print(bheap.findNode(3))
# print(bheap.findNode(5))
# print(bheap.findNode(6))
# print(bheap.findNode(9))
# print(bheap.findNode(2))
# print(bheap.findNode(11))
# print(bheap.findNode(4))
# print('Menu')
# print('insert <data>')
# print('min get')
# print('min extract')
# print('quit')
#
# while True:
#     do = input('What would you like to do? ').split()
#
#     operation = do[0].strip().lower()
#     if operation == 'insert':
#         data = int(do[1])
#         bheap.insert(data)
#     elif operation == 'min':
#         suboperation = do[1].strip().lower()
#         if suboperation == 'get':
#             print('Minimum value: {}'.format(bheap.getMin()))
#         elif suboperation == 'extract':
#             print('Minimum value removed: {}'.format(bheap.extractMin()))
#
#     elif operation == 'quit':
#         break
