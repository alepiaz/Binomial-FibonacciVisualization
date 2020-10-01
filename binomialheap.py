
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

    def combine_roots(self, p):
        self.heap.extend(p.heap)
        self.heap.sort(key = lambda tree : tree.rank)

    def union(self, p):
        self.combine_roots(p)
        if self.heap == []:
            print("Both binomial heap are empty")
            return
        i = 0
        while i < len(self.heap)-1:
            x = self.heap[i]
            succ = self.heap[i+1]
            if x.rank == succ.rank:
                if i+1 < len(self.heap)-1 and self.heap[i+2].rank == succ.rank:
                    nextnext = self.heap[i+2]
                    if succ.k < nextnext.k:
                        succ.addChild(nextnext)
                        del self.heap[i+2]
                    else:
                        nextnext.addChild(succ)
                        del self.heap[i+1]
                else:
                    if x.k < succ.k:
                        x.addChild(succ)
                        del self.heap[i+1]
                    else:
                        succ.addChild(x)
                        del self.heap[i]
            else:
                i+=1
    def insert(self, k):
        y = BinomialHeap(BinomialTree(k))
        self.union(y)

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
        H = BinomialHeap()
        H.heap = min.children
        self.union(H)

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

    def generateDot(self):
        text = generateDot_r(self.heap)
        return text

    def visualizeTree(self):
        dot_text = """digraph G {

          node [margin=0 fontcolor=blue fontsize=15 width=0.5 shape=circle style=filled]
          edge [dir=none]
          %s
        }""" % self.generateDot()
        return dot_text


def generateDot_r(nodes):
    if nodes == []:
        return ""
    text = ""
    for n in nodes:
        for c in n.children:
            text+=str("{0} -> {1}\n".format(n.k,c.k))
        text+=generateDot_r(n.children)
    return text

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
