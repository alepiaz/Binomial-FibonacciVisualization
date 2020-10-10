from graphviz import Source

DOT = """digraph G {
    node [margin=0 fontcolor=blue fontsize=15 width=0.5 shape=circle style=filled]
    edge [dir=none]
    %s
}"""

class Node:

    def __init__(self):
        self.n = None
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibiling = None

class BinomialHeap:

    # def __init__(self):
    #     self.H = self.initializeHeap()
    #     self.Hr = self.initializeHeap()
    #     self.count = 1


    def createNode(self,k):
        p = Node()
        p.n = k
        return p

    def initializeHeap(self):
        return None

    def binomialLink(self,y,z):
        y.parent = z
        y.sibiling = z.child
        z.child = y
        z.degree +=1

    def insert(self,H,x):
        n = self.createNode(x)
        H = self.union(H ,n)
        return H

    def union(self,H1,H2):
        H = self.merge(H1,H2)
        if H == None:
            return H
        prev = None
        x = H
        next = x.sibiling
        while(next != None):
            if ((x.degree != next.degree) or ((next.sibiling != None) and next.sibiling.degree == x.degree)):
                prev = x
                x = next
            else:
                if (x.n <= next.n):
                    x.sibiling = next.sibiling
                    self.binomialLink(next,x)
                else:
                    if (prev == None):
                        H = next
                    else:
                        prev.sibiling = next
                    self.binomialLink(x,next)
                    x = next
            next = x.sibiling

        return H

    def merge(self,H1,H2):
        H = self.initializeHeap()
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
                y = y.sibiling
            elif (y.degree == z.degree):
                tmp = y.sibiling
                y.sibiling = z
                y = tmp
            else:
                tmp = z.sibiling
                z.sibiling = y
                z = tmp

        return H

    def display(self,H):
        if (H == None):
            print("Heap vuoto")
        p = H
        while (p != None):
            print("{0} ".format(p.n))
            p = p.sibiling
        print("\n")

    def search(self, H, k):
        x = H
        p = None
        if (x.n == k):
            p = x
            return p
        if (x.child != None and p == None):
            p = self.search(x.child,k)
        if (x.sibiling != None and p == None):
            p = self.search(x.sibiling,k)

        return p

    def info(self, H):
        x = H
        c = s = p = "None"
        if x:
            if x.child:
                c = x.child.n
            if x.sibiling:
                s = x.sibiling.n
            if x.parent:
                p = x.parent.n
            print("n:{0} c:{1} s:{2} p:{3}".format(x.n,c,s,p))
        if (x.child != None):
            p = self.info(x.child)
        if (x.sibiling != None):
            p = self.info(x.sibiling)


    def generateDot(self, H):
        text = ""
        if (H == None):
            return text
        p = H

        if (p.parent != None):
            text+="{0}->{1}\n".format(p.parent.n,p.n)
        if (p.sibiling != None):
            text=self.generateDot(p.sibiling)+text
        if (p.child != None):
            text+=self.generateDot(p.child)
        if (p.parent == None):
            text="{0} \n".format(p.n)+text
        return text

    def visualizeTree(self,H):
        dot_text = DOT % self.generateDot(H)
        dot = Source(dot_text)
        dot.render("graph","data/cache",format="png")



BH = BinomialHeap()
H = BH.initializeHeap()
H = BH.insert(H,1)
H = BH.insert(H,3)
H = BH.insert(H,5)
H = BH.insert(H,6)
H = BH.insert(H,9)
H = BH.insert(H,2)
H = BH.insert(H,11)
H = BH.insert(H,4)
print(BH.generateDot(H))
BH.visualizeTree(H)
