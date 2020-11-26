# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_ins = QtWidgets.QPushButton(self.centralwidget)
        self.button_ins.setGeometry(QtCore.QRect(190, 30, 100, 28))
        self.button_ins.setObjectName("button_ins")
        self.button_del = QtWidgets.QPushButton(self.centralwidget)
        self.button_del.setGeometry(QtCore.QRect(190, 80, 100, 28))
        self.button_del.setObjectName("button_del")
        self.button_min = QtWidgets.QPushButton(self.centralwidget)
        self.button_min.setGeometry(QtCore.QRect(330, 80, 121, 28))
        self.button_min.setObjectName("button_min")
        self.textbox_ins = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox_ins.setGeometry(QtCore.QRect(60, 30, 113, 28))
        self.textbox_ins.setObjectName("textbox_ins")
        self.textbox_del = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox_del.setGeometry(QtCore.QRect(60, 80, 113, 28))
        self.textbox_del.setObjectName("textbox_del")
        self.bheap = QtWidgets.QLabel(self.centralwidget)
        self.bheap.setGeometry(QtCore.QRect(20, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bheap.setFont(font)
        self.bheap.setObjectName("bheap")
        self.fheap = QtWidgets.QLabel(self.centralwidget)
        self.fheap.setGeometry(QtCore.QRect(540, 160, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.fheap.setFont(font)
        self.fheap.setObjectName("fheap")
        self.timestamp = QtWidgets.QLabel(self.centralwidget)
        self.timestamp.setGeometry(QtCore.QRect(540, 40, 451, 61))
        self.timestamp.setText("")
        self.timestamp.setObjectName("timestamp")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-80, 130, 1201, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(460, 140, 101, 711))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 230, 451, 441))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 449, 439))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(540, 230, 451, 441))
        self.scrollArea_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 449, 439))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_ins.setText(_translate("MainWindow", "Insert"))
        self.button_del.setText(_translate("MainWindow", "Delete"))
        self.button_min.setText(_translate("MainWindow", "Extract Min"))
        self.bheap.setText(_translate("MainWindow", "Binomial Heap"))
        self.fheap.setText(_translate("MainWindow", "Fibonacci Heap"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
