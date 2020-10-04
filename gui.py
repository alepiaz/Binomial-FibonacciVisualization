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
        self.width = 500
        self.height = 480
        self.BHeap = BinomialHeap()
        self.initUI()



    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20,20)
        self.textbox.resize(70,30)

        # Create a button in the window
        self.button = QPushButton('Insert', self)
        self.button.move(100,20)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.textbox.returnPressed.connect(self.on_click)
        self.show()



        self.BHeap.visualizeTree()
        self.label = QLabel(self)
        # self.label.setGeometry(QRect(50,80,300,300))
        self.pixmap = (QPixmap("data/cache/graph.png"))
        self.label.setPixmap(self.pixmap)
        # self.label.setFixedSize(self.pixmap.size())
        self.label.setScaledContents(True)
        self.label.setGeometry(50,120,300,300)
        self.label.show()

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
    def on_click(self):
        textboxValue = self.textbox.text()
        self.BHeap.insert(int(textboxValue))
        self.BHeap.visualizeTree()
        self.pixmap = (QPixmap("data/cache/graph.png"))
        self.label.setPixmap(self.pixmap)
        # self.label.setFixedSize(self.pixmap.size())
        self.label.setScaledContents(True)
        self.label.setGeometry(50,120,300,300)
        self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
