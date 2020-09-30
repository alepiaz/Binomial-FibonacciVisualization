from binomialheap import *

bheap = BinomialHeap()

bheap.insert(1)
# bheap.printAllNodes()
bheap.insert(3)
# bheap.printAllNodes()
bheap.insert(5)
# bheap.printAllNodes()
bheap.insert(6)
# bheap.printAllNodes()
bheap.insert(9)
# bheap.printAllNodes()
bheap.insert(2)
# bheap.printAllNodes()
bheap.insert(11)
# bheap.printAllNodes()
bheap.insert(4)
# bheap.printAllNodes()

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
