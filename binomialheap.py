
class BinomialTree:

    def __init__(self, k):
        self.k = k
        self.children = []
        self.rank = 0
        self.parent = None

    def addChild(self, t):
        self.children.append(t)
        t.parent = self
        self.rank = self.rank + 1


class BinomialHeap:

    def __init__(self, heap = []):
        self.heap = [heap] if heap != [] else heap


    def getMin(self):
        if self.heap ==  []:
            print("Cannot get min from empty heap")
            return None
        min = self.heap[0].k
        for i,_ in enumerate(self.heap):
            if self.heap[i].k < min:
                min = self.heap[i].k
        return min

    def mergeTree(p, q):
        if p.k <= q.k:
            return p.addChild(q)
        else:
            return q.addChild(p)

    def union(self, p):
        # print("p", p)
        self.heap.extend(p)
        if self.heap == []:
            print("Both binomial heap are empty")
            return
        self.heap.sort(key = lambda tree : tree.rank)
        # print(range(0,len(self.heap)-1))
        i = 0
        while i < len(self.heap)-1:
            # print (i)
            x = self.heap[i]
            next = self.heap[i+1]
            if x.rank == next.rank:
                if i < len(self.heap)-2 and self.heap[i+2].rank == next.rank:
                    nextnext = self.heap[i+2]
                    if next.k < nextnext.k:
                        next.addChild(nextnext)
                        del self.heap[i+2]
                    else:
                        nextnext.addChild(next)
                        del self.heap[i+1]
                else:
                    if x.k < next.k:
                        x.addChild(next)
                        del self.heap[i+1]
                    else:
                        next.addChild(x)
                        del self.heap[i]
            i+=1
    def insert(self, k):
        y = BinomialHeap(BinomialTree(k))
        self.union(y.heap)

    def extractMin(self):
        if self.heap == []:
            print("Cannot extract min from empty heap")
            return None

        min = self.heap[0]
        for h in self.heap:
            if h.k < min.k:
                min = h
        self.heap.remove(min)
        y = min.children
        # print ("y",y)
        self.union(y)
        return min.k

    def findNode(self, j):
        node = findNode_r(self.heap, j)
        return node

    def decreaseKey(self, x, h):
        if h > x.k:
            print("New key is greater than current one")
            return
        x.k = h
        y = x
        z = y.parent
        while z != None and y.k < z.k:
            y.k,z.k = (z.k, y.k)
            y = z
            z = y.parent

    # def delete(self, x):
    def printAllNodes(self):
        child_list = []
        for h in self.heap:
            print("\n",h.k,":")
            for c in h.children:
                print(c.k)
                for i in c.children:
                    print(i.k)

def findNode_r(nodes, j):
    if nodes == []:
        return None
    for n in nodes:
        if n.k <= j:
            if n.k == j:
                return n.k
            elif n.children != []:
                return findNode_r(n.children, j)
    return None
