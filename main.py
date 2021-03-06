# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtCore import pyqtSlot, QRect
from PyQt5.QtSvg import QSvgWidget, QSvgRenderer

from heap import *
from main_window import Ui_MainWindow
import time




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.showMaximized()
        self.BHeap = BinomialHeap()
        self.FHeap = FibonacciHeap()
        self.setupUi(self)
        self.radioBF.setChecked(True)
        self.button_ins.clicked.connect(self.insert)
        self.button_del.clicked.connect(self.delete)
        self.button_min.clicked.connect(self.extractMin)
        self.textbox_del.returnPressed.connect(self.delete)
        self.textbox_ins.returnPressed.connect(self.insert)
        self.button_reset.clicked.connect(self.reset)
        self.radioBF.toggled.connect(lambda: self.radio_handler(0))
        self.radioB.toggled.connect(lambda: self.radio_handler(1))
        self.radioF.toggled.connect(lambda: self.radio_handler(2))
        self.textbox_ins.cursorPosition()

    def radio_handler(self, status):
        if status == 0:
            self.line_2.setVisible(True)
            self.binomial_widget.setVisible(True)
            self.fibonacci_widget.setVisible(True)
        else:
            self.line_2.setVisible(False)
            if status == 1:
                self.binomial_widget.setVisible(True)
                self.fibonacci_widget.setVisible(False)
            else:
                self.fibonacci_widget.setVisible(True)
                self.binomial_widget.setVisible(False)

    def reset(self):
        self.BHeap = BinomialHeap()
        self.FHeap = FibonacciHeap()
        self.timestamp.setText("")
        self.BHeap.visualizeTree()
        self.FHeap.visualizeTree()
        self.updateImg()

    def updateImg(self):
        self.BHeap.visualizeTree()
        self.FHeap.visualizeTree()
        self.pixmap = (QPixmap("data/cache/graph.png"))
        self.label.setPixmap(self.pixmap)
        self.pixmap2 = (QPixmap("data/cache/fgraph.png"))
        self.label_2.setPixmap(self.pixmap2)

    def updateText(self, tB, tF):
        self.timestamp.setText("{0}\n{1}".format(tB,tF))

    @pyqtSlot()
    def insert(self):
        textboxValue = self.textbox_ins.text()
        self.textbox_ins.setText("")
        try:
            textboxValue = int(textboxValue)
        except Exception:
            QtWidgets.QMessageBox.about(self, 'Error','Input can only be a number')
            return
        tB = self.BHeap.insert(textboxValue)[1]
        tF = self.FHeap.insert(textboxValue)[1]
        self.updateText(tB,tF)
        self.updateImg()


    def extractMin(self):
        if self.BHeap.H == None:
            QtWidgets.QMessageBox.about(self, 'Error','Heap is empty')
            return
        tB = self.BHeap.extractMin()[1]
        tF = self.FHeap.extractMin()[1]
        self.updateText(tB,tF)
        self.updateImg()

    @pyqtSlot()
    def delete(self):
        textboxValue = self.textbox_del.text()
        self.textbox_del.setText("")
        try:
            textboxValue = int(textboxValue)
        except Exception:
            QtWidgets.QMessageBox.about(self, 'Error','Input can only be a number')
            return
        if self.BHeap.H == None:
            QtWidgets.QMessageBox.about(self, 'Error','Heap is empty')
            return
        if self.BHeap.search(int(textboxValue)) == None:
            QtWidgets.QMessageBox.about(self, 'Error','Cannot find this number into the heap')
            return
        tB = self.BHeap.delete(textboxValue)[1]
        tF = self.FHeap.delete(textboxValue)[1]
        self.updateText(tB,tF)
        self.updateImg()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
