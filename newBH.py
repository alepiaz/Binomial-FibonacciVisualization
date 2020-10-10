from graphviz import Source

DOT = """digraph G {
    node [margin=0 fontcolor=blue fontsize=15 width=0.5 shape=circle style=filled]
    edge [dir=none]
    %s
}"""

class Node:

    def __init__(self, k = None):
        self.n = k
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None

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




    # def initializeHeap(self):
    #     return None

    def binomialLink(self,y,z):
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree +=1

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
        if (x == None):
            x = self.H
        p = None
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
        # self.info(self.Hr)


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
            # x.child.sibling = None
        self.union(H1,self.Hr)
        return x

    def decreaseKey(self,i,k):
        p = self.search(i)
        if (p == None):
            print("Chiave non trovata")
            return
        if (k > p.n):
            print("Il nuovo valore deve essere minore del vecchio")

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

    def delete(self,k):
        if (self.H == None):
            print("L'heap è vuoto")
        self.decreaseKey(k,float("-inf"))
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
        if (x.child != None):
            p = self.info(x.child)
        if (x.sibling != None):
            p = self.info(x.sibling)


    def generateDot(self,H):
        text = ""
        if (H == None):
            return text
        p = H

        if (p.parent != None):
            text+="{0}->{1}\n".format(p.parent.n,p.n)
        if (p.sibling != None):
            text=self.generateDot(p.sibling)+text
        if (p.child != None):
            text+=self.generateDot(p.child)
        if (p.parent == None):
            text="{0} \n".format(p.n)+text
        return text

    def visualizeTree(self, name = "graph"):
        dot_text = DOT % self.generateDot(self.H)
        dot = Source(dot_text)
        dot.render(name,"data/cache",format="png")



BH = BinomialHeap()

BH.insert(1)
BH.insert(3)
BH.insert(5)
BH.insert(6)
BH.insert(9)
BH.insert(2)
BH.insert(11)
BH.insert(4)
BH.insert(19)
# BH.extractMin()
BH.delete(4)
# BH.decreaseKey(3,1)
BH.visualizeTree()
