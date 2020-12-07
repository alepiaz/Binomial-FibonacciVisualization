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
        MainWindow.setEnabled(True)
        MainWindow.resize(1023, 721)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textbox_del = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox_del.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textbox_del.sizePolicy().hasHeightForWidth())
        self.textbox_del.setSizePolicy(sizePolicy)
        self.textbox_del.setMinimumSize(QtCore.QSize(100, 0))
        self.textbox_del.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textbox_del.setObjectName("textbox_del")
        self.horizontalLayout_5.addWidget(self.textbox_del)
        self.button_del = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_del.sizePolicy().hasHeightForWidth())
        self.button_del.setSizePolicy(sizePolicy)
        self.button_del.setObjectName("button_del")
        self.horizontalLayout_5.addWidget(self.button_del)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textbox_ins = QtWidgets.QLineEdit(self.centralwidget)
        self.textbox_ins.setObjectName("textbox_ins")
        self.horizontalLayout_4.addWidget(self.textbox_ins)
        self.button_ins = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_ins.sizePolicy().hasHeightForWidth())
        self.button_ins.setSizePolicy(sizePolicy)
        self.button_ins.setObjectName("button_ins")
        self.horizontalLayout_4.addWidget(self.button_ins)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.button_reset = QtWidgets.QPushButton(self.centralwidget)
        self.button_reset.setObjectName("button_reset")
        self.gridLayout_2.addWidget(self.button_reset, 3, 2, 1, 1)
        self.button_min = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_min.sizePolicy().hasHeightForWidth())
        self.button_min.setSizePolicy(sizePolicy)
        self.button_min.setObjectName("button_min")
        self.gridLayout_2.addWidget(self.button_min, 2, 2, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radioBF = QtWidgets.QRadioButton(self.centralwidget)
        self.radioBF.setObjectName("radioBF")
        self.verticalLayout_5.addWidget(self.radioBF)
        self.radioB = QtWidgets.QRadioButton(self.centralwidget)
        self.radioB.setObjectName("radioB")
        self.verticalLayout_5.addWidget(self.radioB)
        self.radioF = QtWidgets.QRadioButton(self.centralwidget)
        self.radioF.setObjectName("radioF")
        self.verticalLayout_5.addWidget(self.radioF)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_3.addWidget(self.line_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.timestamp = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timestamp.sizePolicy().hasHeightForWidth())
        self.timestamp.setSizePolicy(sizePolicy)
        self.timestamp.setMinimumSize(QtCore.QSize(300, 0))
        self.timestamp.setText("")
        self.timestamp.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.timestamp.setObjectName("timestamp")
        self.horizontalLayout_3.addWidget(self.timestamp)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.centre_layout = QtWidgets.QHBoxLayout()
        self.centre_layout.setObjectName("centre_layout")
        self.binomial_widget = QtWidgets.QWidget(self.centralwidget)
        self.binomial_widget.setObjectName("binomial_widget")
        self.binomial_layout = QtWidgets.QVBoxLayout(self.binomial_widget)
        self.binomial_layout.setObjectName("binomial_layout")
        self.bheap = QtWidgets.QLabel(self.binomial_widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.bheap.setFont(font)
        self.bheap.setObjectName("bheap")
        self.binomial_layout.addWidget(self.bheap)
        self.scrollArea = QtWidgets.QScrollArea(self.binomial_widget)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 489, 558))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.binomial_layout.addWidget(self.scrollArea)
        self.centre_layout.addWidget(self.binomial_widget)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.centre_layout.addWidget(self.line_2)
        self.fibonacci_widget = QtWidgets.QWidget(self.centralwidget)
        self.fibonacci_widget.setObjectName("fibonacci_widget")
        self.fibonacci_layout = QtWidgets.QVBoxLayout(self.fibonacci_widget)
        self.fibonacci_layout.setObjectName("fibonacci_layout")
        self.fheap = QtWidgets.QLabel(self.fibonacci_widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.fheap.setFont(font)
        self.fheap.setObjectName("fheap")
        self.fibonacci_layout.addWidget(self.fheap)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.fibonacci_widget)
        self.scrollArea_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 489, 558))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.fibonacci_layout.addWidget(self.scrollArea_2)
        self.centre_layout.addWidget(self.fibonacci_widget)
        self.verticalLayout_3.addLayout(self.centre_layout)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_del.setText(_translate("MainWindow", "Delete"))
        self.button_ins.setText(_translate("MainWindow", "Insert"))
        self.button_reset.setText(_translate("MainWindow", "Reset"))
        self.button_min.setText(_translate("MainWindow", "Extract Min"))
        self.radioBF.setText(_translate("MainWindow", "Binomial + Fibonacci"))
        self.radioB.setText(_translate("MainWindow", "Fibonacci"))
        self.radioF.setText(_translate("MainWindow", "Binomial"))
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
