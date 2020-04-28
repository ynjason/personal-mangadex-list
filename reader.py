# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reader.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_reader(object):
    def setupUi(self, reader):
        reader.setObjectName("reader")
        reader.resize(804, 596)
        self.centralwidget = QtWidgets.QWidget(reader)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pagelist = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.pagelist.setObjectName("pagelist")
        self.horizontalLayout.addWidget(self.pagelist)
        self.jump = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.jump.setObjectName("jump")
        self.horizontalLayout.addWidget(self.jump)
        self.unread = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.unread.setObjectName("unread")
        self.horizontalLayout.addWidget(self.unread)
        self.read = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.read.setObjectName("read")
        self.horizontalLayout.addWidget(self.read)
        self.previous = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.previous.setObjectName("previous")
        self.horizontalLayout.addWidget(self.previous)
        self.next = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        self.home = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.home.setObjectName("home")
        self.horizontalLayout.addWidget(self.home)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 30, 801, 531))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        reader.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(reader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName("menubar")
        reader.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(reader)
        self.statusbar.setObjectName("statusbar")
        reader.setStatusBar(self.statusbar)

        self.retranslateUi(reader)
        QtCore.QMetaObject.connectSlotsByName(reader)

    def retranslateUi(self, reader):
        _translate = QtCore.QCoreApplication.translate
        reader.setWindowTitle(_translate("reader", "personal-mangadex-list"))
        self.jump.setText(_translate("reader", "Jump to Page"))
        self.unread.setText(_translate("reader", "Mark as unread"))
        self.read.setText(_translate("reader", "Mark as read"))
        self.previous.setText(_translate("reader", "Previous Chapter"))
        self.next.setText(_translate("reader", "Next Chapter"))
        self.home.setText(_translate("reader", "Home"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    reader = QtWidgets.QMainWindow()
    ui = Ui_reader()
    ui.setupUi(reader)
    reader.show()
    sys.exit(app.exec_())
