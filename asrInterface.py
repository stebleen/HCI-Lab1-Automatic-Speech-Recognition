# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 462)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 280, 201, 51))    # 设置当前QWidget的显示位置和大小
        font = QtGui.QFont()    # 创建字体对象
        font.setFamily("Calibri")   # 设置字体类型
        font.setPointSize(14)   # 设置文字大小
        self.label_3.setFont(font)  # 设置字体
        self.label_3.setStyleSheet("color: rgb(0, 117, 210);")  # 设置控件的样式(QSS)
        self.label_3.setWordWrap(True)  # 设置Label标签文本换行显示
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 250, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")

        # label_5
        self.label_5 = QtWidgets.QLabel(self.centralwidget) #创建label_5控件
        self.label_5.setGeometry(QtCore.QRect(60, 400, 201, 21))    # 设置当前QWidget的显示位置和大小
        font = QtGui.QFont()    # 创建字体对象
        font.setFamily("Calibri")   # 设置字体类型
        font.setPointSize(12)   # 设置文字大小
        self.label_5.setFont(font)  # 设置字体
        self.label_5.setStyleSheet("color: rgb(100, 200, 200);")    # 设置控件的样式(QSS)
        self.label_5.setWordWrap(True)  # 设置Label标签文本换行显示
        self.label_5.setObjectName("label_5")   # 为控件设置一个名称，当作控件的ID来使用。

        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(70, 50, 161, 121))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        # # play.gif
        # self.playVoice = QtWidgets.QLabel(self.centralwidget)
        # self.playVoice.setGeometry(QtCore.QRect(70, 20, 161, 121))
        # self.playVoice.setText("")
        # self.gif = QMovie("icon/play.gif")
        # self.playVoice.setMovie(self.gif)
        # self.gif.start()
        # self.playVoice.setScaledContents(True)
        # self.playVoice.setObjectName("playVoice")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 160, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 330, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.label_3.setText(_translate("MainWindow", "1. Enjoy music by saying \"Play music\""))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_4.setText(_translate("MainWindow", "2. Take some notes by saying \"Open Notepad\""))

    def words(self, mywords):
        # 在窗口上显示说的话
        _translate = QtCore.QCoreApplication.translate
        self.label_5.setText(_translate("MainWindow", mywords))