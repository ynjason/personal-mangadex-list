# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gui(object):
    def setupUi(self, gui):
        gui.setObjectName("gui")
        gui.resize(804, 626)
        self.centralwidget = QtWidgets.QWidget(gui)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 611))
        self.tabWidget.setObjectName("tabWidget")
        self.CurrentlyReading = QtWidgets.QWidget()
        self.CurrentlyReading.setObjectName("CurrentlyReading")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.CurrentlyReading)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 60, 791, 41))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.Urladd_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.Urladd_1.setContentsMargins(0, 0, 0, 0)
        self.Urladd_1.setObjectName("Urladd_1")
        self.urlText_1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.urlText_1.setObjectName("urlText_1")
        self.Urladd_1.addWidget(self.urlText_1)
        self.url_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.url_1.setObjectName("url_1")
        self.Urladd_1.addWidget(self.url_1)
        self.Description_1 = QtWidgets.QScrollArea(self.CurrentlyReading)
        self.Description_1.setGeometry(QtCore.QRect(0, 100, 791, 461))
        self.Description_1.setWidgetResizable(True)
        self.Description_1.setObjectName("Description_1")
        self.DescriptionContents_1 = QtWidgets.QWidget()
        self.DescriptionContents_1.setGeometry(QtCore.QRect(0, 0, 789, 459))
        self.DescriptionContents_1.setObjectName("DescriptionContents_1")
        self.Description_1.setWidget(self.DescriptionContents_1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.CurrentlyReading)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.ChooseManga_1 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget)
        self.ChooseManga_1.setContentsMargins(0, 0, 0, 0)
        self.ChooseManga_1.setObjectName("ChooseManga_1")
        self.Mangaselect_1 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.Mangaselect_1.setObjectName("Mangaselect_1")
        self.ChooseManga_1.addWidget(self.Mangaselect_1)
        self.Select_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Select_1.setObjectName("Select_1")
        self.ChooseManga_1.addWidget(self.Select_1)
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.CurrentlyReading)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(500, 0, 202, 61))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.movegrid_1 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.movegrid_1.setContentsMargins(0, 0, 0, 0)
        self.movegrid_1.setObjectName("movegrid_1")
        self.category_1 = QtWidgets.QComboBox(self.gridLayoutWidget_5)
        self.category_1.setObjectName("category_1")
        self.category_1.addItem("")
        self.category_1.addItem("")
        self.movegrid_1.addWidget(self.category_1, 0, 1, 1, 1)
        self.confirmmove_1 = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.confirmmove_1.setObjectName("confirmmove_1")
        self.movegrid_1.addWidget(self.confirmmove_1, 1, 1, 1, 1)
        self.MoveCategories_1 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.MoveCategories_1.setObjectName("MoveCategories_1")
        self.movegrid_1.addWidget(self.MoveCategories_1, 1, 0, 1, 1)
        self.manga_1 = QtWidgets.QComboBox(self.gridLayoutWidget_5)
        self.manga_1.setObjectName("manga_1")
        self.movegrid_1.addWidget(self.manga_1, 0, 0, 1, 1)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.CurrentlyReading)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(710, 0, 81, 61))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.updateanddownload_1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.updateanddownload_1.setContentsMargins(0, 0, 0, 0)
        self.updateanddownload_1.setObjectName("updateanddownload_1")
        self.downloadnew_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.downloadnew_1.setObjectName("downloadnew_1")
        self.updateanddownload_1.addWidget(self.downloadnew_1)
        self.updateall_1 = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.updateall_1.setObjectName("updateall_1")
        self.updateanddownload_1.addWidget(self.updateall_1)
        self.tabWidget.addTab(self.CurrentlyReading, "")
        self.ToTry = QtWidgets.QWidget()
        self.ToTry.setObjectName("ToTry")
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.ToTry)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(0, 0, 501, 61))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.ChooseManga_2 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_10)
        self.ChooseManga_2.setContentsMargins(0, 0, 0, 0)
        self.ChooseManga_2.setObjectName("ChooseManga_2")
        self.Mangaselect_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_10)
        self.Mangaselect_2.setObjectName("Mangaselect_2")
        self.ChooseManga_2.addWidget(self.Mangaselect_2)
        self.Select_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_10)
        self.Select_2.setObjectName("Select_2")
        self.ChooseManga_2.addWidget(self.Select_2)
        self.Description_2 = QtWidgets.QScrollArea(self.ToTry)
        self.Description_2.setGeometry(QtCore.QRect(0, 100, 791, 461))
        self.Description_2.setWidgetResizable(True)
        self.Description_2.setObjectName("Description_2")
        self.DescriptionContents_2 = QtWidgets.QWidget()
        self.DescriptionContents_2.setGeometry(QtCore.QRect(0, 0, 789, 459))
        self.DescriptionContents_2.setObjectName("DescriptionContents_2")
        self.Description_2.setWidget(self.DescriptionContents_2)
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.ToTry)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(500, 0, 202, 61))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.movegrid_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.movegrid_2.setContentsMargins(0, 0, 0, 0)
        self.movegrid_2.setObjectName("movegrid_2")
        self.category_2 = QtWidgets.QComboBox(self.gridLayoutWidget_6)
        self.category_2.setObjectName("category_2")
        self.category_2.addItem("")
        self.category_2.addItem("")
        self.movegrid_2.addWidget(self.category_2, 0, 1, 1, 1)
        self.confirmmove_2 = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.confirmmove_2.setObjectName("confirmmove_2")
        self.movegrid_2.addWidget(self.confirmmove_2, 1, 1, 1, 1)
        self.MoveCategories_2 = QtWidgets.QLabel(self.gridLayoutWidget_6)
        self.MoveCategories_2.setObjectName("MoveCategories_2")
        self.movegrid_2.addWidget(self.MoveCategories_2, 1, 0, 1, 1)
        self.manga_2 = QtWidgets.QComboBox(self.gridLayoutWidget_6)
        self.manga_2.setObjectName("manga_2")
        self.movegrid_2.addWidget(self.manga_2, 0, 0, 1, 1)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.ToTry)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(710, 0, 81, 61))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.updateanddownload_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.updateanddownload_2.setContentsMargins(0, 0, 0, 0)
        self.updateanddownload_2.setObjectName("updateanddownload_2")
        self.downloadnew_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_11)
        self.downloadnew_2.setObjectName("downloadnew_2")
        self.updateanddownload_2.addWidget(self.downloadnew_2)
        self.updateall_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_11)
        self.updateall_2.setObjectName("updateall_2")
        self.updateanddownload_2.addWidget(self.updateall_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.ToTry)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 60, 791, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.Urladd_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.Urladd_2.setContentsMargins(0, 0, 0, 0)
        self.Urladd_2.setObjectName("Urladd_2")
        self.urlText_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.urlText_2.setObjectName("urlText_2")
        self.Urladd_2.addWidget(self.urlText_2)
        self.url_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.url_2.setObjectName("url_2")
        self.Urladd_2.addWidget(self.url_2)
        self.tabWidget.addTab(self.ToTry, "")
        self.Completed = QtWidgets.QWidget()
        self.Completed.setObjectName("Completed")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.Completed)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(500, 0, 202, 61))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.movegrid_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.movegrid_3.setContentsMargins(0, 0, 0, 0)
        self.movegrid_3.setObjectName("movegrid_3")
        self.category_3 = QtWidgets.QComboBox(self.gridLayoutWidget_7)
        self.category_3.setObjectName("category_3")
        self.category_3.addItem("")
        self.category_3.addItem("")
        self.movegrid_3.addWidget(self.category_3, 0, 1, 1, 1)
        self.confirmmove_3 = QtWidgets.QPushButton(self.gridLayoutWidget_7)
        self.confirmmove_3.setObjectName("confirmmove_3")
        self.movegrid_3.addWidget(self.confirmmove_3, 1, 1, 1, 1)
        self.MoveCategories_3 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.MoveCategories_3.setObjectName("MoveCategories_3")
        self.movegrid_3.addWidget(self.MoveCategories_3, 1, 0, 1, 1)
        self.manga_3 = QtWidgets.QComboBox(self.gridLayoutWidget_7)
        self.manga_3.setObjectName("manga_3")
        self.movegrid_3.addWidget(self.manga_3, 0, 0, 1, 1)
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.Completed)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(0, 0, 501, 61))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.ChooseManga_3 = QtWidgets.QHBoxLayout(self.verticalLayoutWidget_13)
        self.ChooseManga_3.setContentsMargins(0, 0, 0, 0)
        self.ChooseManga_3.setObjectName("ChooseManga_3")
        self.Mangaselect_3 = QtWidgets.QComboBox(self.verticalLayoutWidget_13)
        self.Mangaselect_3.setObjectName("Mangaselect_3")
        self.ChooseManga_3.addWidget(self.Mangaselect_3)
        self.Select_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_13)
        self.Select_3.setObjectName("Select_3")
        self.ChooseManga_3.addWidget(self.Select_3)
        self.Description_3 = QtWidgets.QScrollArea(self.Completed)
        self.Description_3.setGeometry(QtCore.QRect(0, 100, 791, 461))
        self.Description_3.setWidgetResizable(True)
        self.Description_3.setObjectName("Description_3")
        self.DescriptionContents_3 = QtWidgets.QWidget()
        self.DescriptionContents_3.setGeometry(QtCore.QRect(0, 0, 789, 459))
        self.DescriptionContents_3.setObjectName("DescriptionContents_3")
        self.Description_3.setWidget(self.DescriptionContents_3)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.Completed)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(710, 0, 81, 61))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.updateanddownload_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.updateanddownload_3.setContentsMargins(0, 0, 0, 0)
        self.updateanddownload_3.setObjectName("updateanddownload_3")
        self.downloadnew_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_12)
        self.downloadnew_3.setObjectName("downloadnew_3")
        self.updateanddownload_3.addWidget(self.downloadnew_3)
        self.updateall_3 = QtWidgets.QPushButton(self.verticalLayoutWidget_12)
        self.updateall_3.setObjectName("updateall_3")
        self.updateanddownload_3.addWidget(self.updateall_3)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.Completed)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 60, 791, 41))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.Urladd_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.Urladd_3.setContentsMargins(0, 0, 0, 0)
        self.Urladd_3.setObjectName("Urladd_3")
        self.urlText_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.urlText_3.setObjectName("urlText_3")
        self.Urladd_3.addWidget(self.urlText_3)
        self.url_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.url_3.setObjectName("url_3")
        self.Urladd_3.addWidget(self.url_3)
        self.tabWidget.addTab(self.Completed, "")
        gui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(gui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName("menubar")
        gui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(gui)
        self.statusbar.setObjectName("statusbar")
        gui.setStatusBar(self.statusbar)

        self.retranslateUi(gui)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(gui)

    def retranslateUi(self, gui):
        _translate = QtCore.QCoreApplication.translate
        gui.setWindowTitle(_translate("gui", "personal-mangadex-list"))
        self.urlText_1.setText(_translate("gui", "Mangadex url to add manga to list"))
        self.Select_1.setText(_translate("gui", "Select"))
        self.category_1.setWhatsThis(_translate("gui", "<html><head/><body><p><br/></p></body></html>"))
        self.category_1.setItemText(0, _translate("gui", "To Try"))
        self.category_1.setItemText(1, _translate("gui", "Completed"))
        self.confirmmove_1.setText(_translate("gui", "Move"))
        self.MoveCategories_1.setText(_translate("gui", "Move Categories"))
        self.downloadnew_1.setText(_translate("gui", "Download New"))
        self.updateall_1.setText(_translate("gui", "Update All"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CurrentlyReading), _translate("gui", "Currently Reading"))
        self.Select_2.setText(_translate("gui", "Select"))
        self.category_2.setWhatsThis(_translate("gui", "<html><head/><body><p><br/></p></body></html>"))
        self.category_2.setItemText(0, _translate("gui", "Currently Reading"))
        self.category_2.setItemText(1, _translate("gui", "Completed"))
        self.confirmmove_2.setText(_translate("gui", "Move"))
        self.MoveCategories_2.setText(_translate("gui", "Move Categories"))
        self.downloadnew_2.setText(_translate("gui", "Download New"))
        self.updateall_2.setText(_translate("gui", "Update All"))
        self.urlText_2.setText(_translate("gui", "Mangadex url to add manga to list"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ToTry), _translate("gui", "To Try"))
        self.category_3.setWhatsThis(_translate("gui", "<html><head/><body><p><br/></p></body></html>"))
        self.category_3.setItemText(0, _translate("gui", "Currently Reading"))
        self.category_3.setItemText(1, _translate("gui", "To Try"))
        self.confirmmove_3.setText(_translate("gui", "Move"))
        self.MoveCategories_3.setText(_translate("gui", "Move Categories"))
        self.Select_3.setText(_translate("gui", "Select"))
        self.downloadnew_3.setText(_translate("gui", "Download New"))
        self.updateall_3.setText(_translate("gui", "Update All"))
        self.urlText_3.setText(_translate("gui", "Mangadex url to add manga to list"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Completed), _translate("gui", "Completed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = QtWidgets.QMainWindow()
    ui = Ui_gui()
    ui.setupUi(gui)
    gui.show()
    sys.exit(app.exec_())