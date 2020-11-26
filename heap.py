from graphviz import Source
import math
from datetime import datetime
import time
import sys

DOT = """digraph G {
    node [margin=0 fontcolor=blue fontsize=15 width=0.5 shape=circle style=filled]
    edge [dir=none]
    %s
}"""


def timing(f):
    time1 = None
    time2 = None
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        text = ('%s function took %.3f ms' % (f.__qualname__, ((time2-time1)*1000.0)))
        return ret, text
    return wrap

class Node:

    def __init__(self, k = None):
        self.n = k
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None
        self.left = None
        self.right = None
        self.mark = False

    def findMinNode(self):
        x = y = self

        min = x.n
        while (x != None):
            if (x.n < min):
                y = x
                min = x.n
            x = x.sibling
        return y

    def reverse(self,sib):
        ret = Node()
        if (self.sibling != None):
            ret = self.sibling.reverse(self)
        else:
            ret = self
        sibling = sib
        return ret

class BinomialHeap:

    def __init__(self):
        self.H = None
        self.Hr = None


    def binomialLink(self,y,z):
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree +=1

    @timing
    def insert(self,x):
        n = Node(x)
        self.union(self.H,n)
        return self

    def union(self,H1,H2):
        H = self.merge(H1,H2)
        if H == None:
            self.H = H
            return
        prev = None
        x = H
        next = x.sibling
        while(next != None):
            if ((x.degree != next.degree) or ((next.sibling != None) and next.sibling.degree == x.degree)):
                prev = x
                x = next
            else:
                if (x.n <= next.n):
                    x.sibling = next.sibling
                    self.binomialLink(next,x)
                else:
                    if (prev == None):
                        H = next
                    else:
                        prev.sibling = next
                    self.binomialLink(x,next)
                    x = next
            next = x.sibling

        self.H = H

    def merge(self,H1,H2):
        H = None
        y = H1
        z = H2
        if (y != None):
            if (z != None):
                if (y.degree <= z.degree):
                    H = y
                else:
                    H = z
            else:
                H = y
        else:
            H = z

        while (y != None and z != None):
            if (y.degree < z.degree):
                y = y.sibling
            elif (y.degree == z.degree):
                tmp = y.sibling
                y.sibling = z
                y = tmp
            else:
                tmp = z.sibling
                z.sibling = y
                z = tmp

        return H

    def search(self, k, x = None):
        p = None
        
        if self.H != None:
            if (x == None):
                x = self.H
            if (x.n == k):
                p = x
                return p
            if (x.child != None and p == None):
                p = self.search(k, x.child)
            if (x.sibling != None and p == None):
                p = self.search(k, x.sibling)

        return p

    def revert_list(self,y):
        x = y
        prev = tmp = None
        while (x != None):
            x.parent = None
            next = x.sibling
            x.sibling = prev
            prev = x
            x = next
        y = prev

        self.Hr = y

    @timing
    def extractMin(self, H1 = None):
        if H1 == None:
            H1 = self.H

        t = None
        self.Hr = None
        x = H1
        if (x == None):
            print("Heap vuoto")
            return x
        min = x.n
        p = x
        while (p.sibling != None):
            if (p.sibling.n < min):
                min = p.sibling.n
                t = p
                x = p.sibling
            p = p.sibling
        if (t == None and x.sibling == None):
            H1 = None
        elif (t == None):
            H1 = x.sibling
        elif (t.sibling == None):
            t = None
        else:
            t.sibling = x.sibling
        if (x.child != None):
            self.revert_list(x.child)
            x.child.sibling = None
        self.union(H1,self.Hr)
        return x

    def decreaseKey(self,i,k):
        p = self.search(i)
        if (p == None):
            print("Chiave non trovata")
            return None
        if (k > p.n):
            print("Il nuovo valore deve essere minore del vecchio")
            return 1

        p.n = k
        y = p
        z = p.parent
        tmp = 0
        while (z != None and y.n < z.n):
            tmp = y.n
            y.n = z.n
            z.n = tmp
            y = z
            z = z.parent
        return p

    def delete(self,k):
        if (self.H == None):
            print("L'heap è vuoto")
            return
        d = self.decreaseKey(k,-sys.maxsize)
        if not d:
            return
        self.extractMin()


    def info(self, H = None):
        if (H == None):
            H = self.H
        x = H
        c = s = p = "None"
        if x:
            if x.child:
                c = x.child.n
            if x.sibling:
                s = x.sibling.n
            if x.parent:
                p = x.parent.n
            print("n:{0} c:{1} s:{2} p:{3}".format(x.n,c,s,p))


    def generateDot(self,H):
        text = ""
        if (H == None):
            return text
        p = H

        if (p.parent != None):
            text+="{0}->{1}\n".format(str(id(p.parent)),str(id(p)))
            text+= "{0} [label={1}]\n".format(str(id(p.parent)),p.parent.n)
            text+= "{0} [label={1}]\n".format(str(id(p)),p.n)
        if (p.sibling != None):
            text=self.generateDot(p.sibling)+text
        if (p.child != None):
            text+=self.generateDot(p.child)
        if (p.parent == None):
            text+= "{0} [label={1}]\n".format(str(id(p)),p.n)

        return text

    def visualizeTree(self, name = "graph"):
        dot_text = DOT % self.generateDot(self.H)
        dot = Source(dot_text)
        dot.render(name,"data/cache",format="png")


class FibonacciHeap:

    H, min = None, None
    nH = 0

    def iterate(self, head):
        node = stop = head
        flag = False
        while True:
            if node == stop and flag is True:
                break
            elif node == stop:
                flag = True
            yield node
            node = node.left

    def findMin(self):
        return self.min

    def mergeRootList(self,n):
        if (self.H == None):
            self.H = n
        else:
            n.right = self.H.right
            n.left = self.H
            self.H.right.left = n
            self.H.right = n

    def mergeChildList(self,p,n):
        if (p.child == None):
            p.child = n
        else:
            n.right = p.child.right
            n.left = p.child
            p.child.right.left = n
            p.child.right = n

    def removeRootList(self, n):
        if (n == self.H):
            self.H = n.left
        n.left.right = n.right
        n.right.left = n.left

    @timing
    def insert(self, k):
        x = Node(k)
        x.left = x.right = x
        self.mergeRootList(x)
        if (self.min == None or x.n < self.min.n):
            self.min = x
        self.nH += 1
        return self


    def fibonacciLink(self,x,y):
        self.removeRootList(y)
        y.left = y.right = y
        self.mergeChildList(x,y)
        x.degree += 1
        y.parent = x
        y.mark = False


    def merge(self, h2):
        H = FibonacciHeap()
        H.H, H.min = self.H, self.min
        # fix pointers when merging the two heaps
        last = h2.H.left
        h2.H.left = H.H.left
        H.H.left.right = h2.H
        H.H.left = last
        H.H.left.right = H.H
        # update min node if needed
        if h2.min.key < H.min.key:
            H.min = h2.min
        # update total nodes
        H.nH = self.nH + h2.nH
        return H

    def display(self):
        p = self.H
        if (p == None):
            print("L'heap è vuoto")
            return
        start = p
        p = p.right
        while (p != start):
            print("-->{0}".format(p.n))
            p = p.right


        print("")

    @timing
    def extractMin(self):
        z = self.min
        if (z != None):
            if(z.child != None):
                children = [x for x in self.iterate(z.child)]
                for i in range(0, len(children)):
                    self.mergeRootList(children[i])
                    children[i].parent = None
            self.removeRootList(z)
            if (z == z.right):
                self.min = self.H = None
            else:
                self.min = z.left
                self.consolidate()
            self.nH -= 1
        return z

    def consolidate(self):
        A = [None] * int(math.log(self.nH)*2)
        nodes = [w for w in self.iterate(self.H)]
        for w in range(0, len(nodes)):
            x = nodes[w]
            d = x.degree
            while A[d] != None:
                y = A[d]
                if (x.n > y.n):
                    tmp = x
                    x,y = y,tmp
                # self.visualizeTree("here")
                self.fibonacciLink(x,y)
                A[d] = None
                d += 1
            A[d] = x
        for i in range(0, len(A)):
            if (A[i] != None):
                if (A[i].n < self.min.n):
                    self.min = A[i]


    def cut(self, x, y):
        self.removeChildList(y, x)
        y.degree -= 1
        self.mergeRootList(x)
        x.parent = None
        x.mark = False



    def cascadingCut(self, y):
        z = y.parent
        if (z != None):
            if y.mark is False:
                y.mark = True
            else:
                self.cut(y, z)
                self.cascadingCut(z)


    def search(self,x):
        stack = []
        stack.append(self.min)
        while (stack):
            curr = stack.pop()
            if (curr.n == x):
                return curr
            else:
                if (curr.child != None):
                    stack.append(curr.child)
                start = curr
                curr = curr.right
                while (curr != start):
                    if (curr.child != None):
                        stack.append(curr.child)
                    if (curr.n == x):
                        return curr
                    curr = curr.right
        return None


    def decreaseKey(self,h,k):
        x = self.search(h)
        if (x):
            if (k > x.n):
                return None
                print("La nuova chiave deve essere minore della chiave attuale")
            x.n = k
            y = x.parent
            if (y != None and x.n < y.n):
                self.cut(x,y)
                self.cascadingCut(y)
            if (x.n < self.min.n):
                self.min = x
            return 1
        else:
            return 0

    def removeChildList(self, parent, node):
        if (parent.child == parent.child.right):
            parent.child = None
        elif (parent.child == node):
            parent.child = node.right
            node.right.parent = parent
        node.left.right = node.right
        node.right.left = node.left


    def delete(self,x):

        d = self.decreaseKey(x,-sys.maxsize)
        if d:
            self.extractMin()


    def info(self,x = None):
        if (x == None):
            x = self.H
        r = l = p = c = ""
        if (x.right):
            r = x.right.n
        if (x.left):
            l = x.left.n
        if (x.parent):
            p = x.parent.n
        if (x.child):
            c = x.child.n
        print("self:{0} right:{1} left:{2} parent:{3} child:{4}".format(x.n,r,l,p,c))

    def visualizeTree(self, name = "fgraph"):
        dot_text = DOT % self.generateDot(self.H, self.H)
        dot = Source(dot_text)
        dot.render(name,"data/cache",format="png")

    def generateDot(self,H,S):
        text = ""
        if (H == None):
            return text
        p = H
        s = S
        if (p.parent != None):
            text+="{0}->{1}\n".format(str(id(p.parent)),str(id(p)))
            text+= "{0} [label={1}]\n".format(str(id(p.parent)),p.parent.n)
            text+= "{0} [label={1}]\n".format(str(id(p)),p.n)
        if (p.left != None and s != p.left):
            text+=self.generateDot(p.left,s)
        if (p.child != None):
            text+=self.generateDot(p.child,p.child)
        if (p.parent == None):
            text+= "{0} [label={1}]\n".format(str(id(p)),p.n)
        return text


B = BinomialHeap()

B.insert(1)
B.delete(1)
B.visualizeTree()
