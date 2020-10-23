import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtCore import pyqtSlot, QRect
from PyQt5.QtSvg import QSvgWidget, QSvgRenderer
from binomialheap import *

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Binomial heap visualization'
        self.left = 10
        self.top = 10
        self.width = 900
        self.height = 460
        self.BHeap = BinomialHeap()
        self.FHeap = FibonacciHeap()
        self.initUI()



    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox_ins = QLineEdit(self)
        self.textbox_ins.move(20,20)
        self.textbox_ins.resize(70,30)

        self.textbox_del = QLineEdit(self)
        self.textbox_del.move(20,50)
        self.textbox_del.resize(70,30)

        # Create a button in the window
        self.button_ins = QPushButton('Insert', self)
        self.button_ins.move(100,20)
        self.button_del = QPushButton('Delete', self)
        self.button_del.move(100,50)
        # connect button to function on_click
        self.button_ins.clicked.connect(self.insert)
        self.button_del.clicked.connect(self.delete)
        self.textbox_ins.returnPressed.connect(self.insert)
        self.textbox_del.returnPressed.connect(self.delete)
        self.show()



        self.BHeap.visualizeTree()
        self.FHeap.visualizeTree()
        self.label = QLabel(self)
        self.label2 = QLabel(self)
        # self.label.setGeometry(QRect(50,80,300,300))
        self.pixmap = (QPixmap("data/cache/graph.png"))
        self.pixmap2 = (QPixmap("data/cache/fgraph.png"))
        self.label.setPixmap(self.pixmap)
        self.label2.setPixmap(self.pixmap2)
        # self.label.setFixedSize(self.pixmap.size())
        self.label.setScaledContents(True)
        self.label.setGeometry(50,120,300,300)
        self.label.show()
        self.label2.setScaledContents(True)
        self.label2.setGeometry(450,120,300,300)
        self.label2.show()

        # self.label.setPixmap(self.qp)
        # self.setCentralWidget(self.label)
        # self.qp.show()


        # self.svgWidget = QSvgWidget(self)
        # self.svgWidget.move(50,80)
        # self.svgWidget.setMaximumSize(300,300)
        # # self.svgWidget.setGeometry(50,80,300,300)
        # self.svgWidget.load('data/cache/graph.svg')
        # self.svgWidget.show()
        # svgWidget.show()

    @pyqtSlot()
    def insert(self):
        textboxValue = self.textbox_ins.text()
        self.BHeap.insert(int(textboxValue))
        self.BHeap.visualizeTree()
        self.FHeap.insert(int(textboxValue))
        self.FHeap.visualizeTree()
        self.pixmap = (QPixmap("data/cache/graph.png"))
        self.label.setPixmap(self.pixmap)
        self.label.setFixedSize(self.pixmap.size())
        self.label.setScaledContents(True)
        self.label.setGeometry(50,120,300,300)
        self.pixmap2 = (QPixmap("data/cache/fgraph.png"))
        self.label2.setPixmap(self.pixmap2)
        self.label2.setFixedSize(self.pixmap2.size())
        self.label2.setScaledContents(True)
        self.label2.setGeometry(450,120,300,300)
        self.textbox_ins.setText("")

    @pyqtSlot()
    def delete(self):
        textboxValue = self.textbox_del.text()
        self.BHeap.delete(int(textboxValue))
        self.BHeap.visualizeTree()
        self.FHeap.delete(int(textboxValue))
        self.FHeap.visualizeTree()
        self.pixmap = (QPixmap("data/cache/graph.png"))
        self.label.setPixmap(self.pixmap)
        self.label.setFixedSize(self.pixmap.size())
        self.label.setScaledContents(True)
        self.label.setGeometry(50,120,300,300)
        self.pixmap2 = (QPixmap("data/cache/fgraph.png"))
        self.label2.setPixmap(self.pixmap2)
        self.label2.setFixedSize(self.pixmap2.size())
        self.label2.setScaledContents(True)
        self.label2.setGeometry(450,120,300,300)
        self.textbox_ins.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
