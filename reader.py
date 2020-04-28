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
        reader.resize(891, 641)
        self.centralwidget = QtWidgets.QWidget(reader)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pagelist = QtWidgets.QComboBox(self.centralwidget)
        self.pagelist.setObjectName("pagelist")
        self.horizontalLayout.addWidget(self.pagelist)
        self.jump = QtWidgets.QPushButton(self.centralwidget)
        self.jump.setObjectName("jump")
        self.horizontalLayout.addWidget(self.jump)
        self.unread = QtWidgets.QPushButton(self.centralwidget)
        self.unread.setObjectName("unread")
        self.horizontalLayout.addWidget(self.unread)
        self.read = QtWidgets.QPushButton(self.centralwidget)
        self.read.setObjectName("read")
        self.horizontalLayout.addWidget(self.read)
        self.previous = QtWidgets.QPushButton(self.centralwidget)
        self.previous.setObjectName("previous")
        self.horizontalLayout.addWidget(self.previous)
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        self.home = QtWidgets.QPushButton(self.centralwidget)
        self.home.setObjectName("home")
        self.horizontalLayout.addWidget(self.home)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 871, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        reader.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(reader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 891, 21))
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
