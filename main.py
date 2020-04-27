from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic, QtGui
from download import dl, float_conversion
from update import update_all_mangas
from gui import Ui_gui
import cloudscraper
import time, os, sys, re, json, html
import sys

def find_manga(manga_list, title):
    for manga in manga_list:
        if manga['title'] == title:
            return manga

def get_coverimg(url):
    scraper = cloudscraper.create_scraper()
    r = scraper.get(url)
    while r.status_code != 200:
        r = scraper.get(url)
    with open('cover_img.png', 'wb+') as f:
        f.write(r.content)

def getchapterlist(manga_dict):
    scraper = cloudscraper.create_scraper()
    try:
        print(manga_dict['url'])
        r = scraper.get(manga_dict["url"])
        print(r)
        manga = json.loads(r.text)
        print(manga)
    except (json.decoder.JSONDecodeError, ValueError) as err:
        print("CloudFlare error: {}".format(err))
        exit(1)

    # check available chapters
    chapters = []

    if "chapter" not in manga:
        print("Chapter not found in the language you requested.")
        exit(1)

    for chap in manga["chapter"]:
        if manga["chapter"][str(chap)]["lang_code"] == "gb":
            chapters.append(manga["chapter"][str(chap)]["chapter"])
    chapters.sort(key=float_conversion) # sort numerically by chapter #

    chapters_revised = ["Oneshot" if x == "" else x for x in chapters]
    return chapters_revised

class Main(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        with open('profile.json', 'r') as infile:
            print("here")
            self.profile = json.load(infile)

        self.gui = Ui_gui()
        self.gui.setupUi(self)
        self.populate_combo_box()
        self.gui.btn_grp = QtWidgets.QButtonGroup()
        self.gui.btn_grp.setExclusive(True)
        self.gui.btn_grp.addButton(self.gui.Select_1)
        self.gui.btn_grp.addButton(self.gui.Select_2)
        self.gui.btn_grp.addButton(self.gui.Select_3)
        self.gui.btn_grp.buttonClicked.connect(self.handle_select_click)
    
    def populate_combo_box(self):
        for types, mangas in enumerate(self.profile):
            if types == 0:
                self.gui.tabWidget.setCurrentIndex(0)
                combobox = self.gui.tabWidget.findChild(QtWidgets.QComboBox, "Mangaselect_1")
                comboboxmove = self.gui.tabWidget.findChild(QtWidgets.QComboBox, "manga_1")
            elif types == 1:
                self.gui.tabWidget.setCurrentIndex(1)
                combobox = self.gui.tabWidget.findChild(QtWidgets.QComboBox, "Mangaselect_2")
                comboboxmove = self.gui.tabWidget.findChild(QtWidgets.QComboBox, "manga_2")
            else:
                self.gui.tabWidget.setCurrentIndex(2)
                combobox = self.gui.tabWidget.findChild(QtWidgets.QComboBox, "Mangaselect_3")
                comboboxmove = self.gui.tabWidget.findChild(QtWidgets.QComboBox, "manga_3")
            for manga in mangas:
                for combox in [combobox, comboboxmove]:
                    combox.addItem(manga['title'])
        self.gui.tabWidget.setCurrentIndex(0)


    def handle_select_click(self, btn):
        print(btn.text())
        tabindex = self.gui.tabWidget.currentIndex()
        findcombo = "Mangaselect_" + str(tabindex+1)
        selectcombo = self.gui.tabWidget.findChild(QtWidgets.QComboBox, findcombo)
        findmanga = selectcombo.currentText()
        manga = find_manga(self.profile[tabindex], findmanga)

        description = "Description_" + str(tabindex+1)
        scrollarea = self.gui.tabWidget.findChild(QtWidgets.QScrollArea, description)

        self.gui.scrollwidget = QWidget(scrollarea)
        self.gui.scrollvbox = QVBoxLayout(self.gui.scrollwidget)

        get_coverimg(manga['cover_url'])
            
        self.gui.cover_img = QtGui.QPixmap("cover_img.png")
        self.gui.cover_img = self.gui.cover_img.scaledToWidth(256)
        self.gui.coverimglabel = QtWidgets.QLabel()
        self.gui.coverimglabel.setPixmap(self.gui.cover_img)
        self.gui.scrollvbox.addWidget(self.gui.coverimglabel)

        self.gui.mangadescription = QLabel(manga['description'])
        self.gui.scrollvbox.addWidget(self.gui.mangadescription)

        self.gui.mangadescription = QLabel("recently read chapter: " + str(manga['recent_read']))
        self.gui.scrollvbox.addWidget(self.gui.mangadescription)

        chapters = getchapterlist(manga)
        print(chapters)

        self.gui.mangadescription = QLabel(manga['description'])
        self.gui.scrollvbox.addWidget(self.gui.mangadescription)

        self.gui.mangadescription = QLabel(manga['description'])
        self.gui.scrollvbox.addWidget(self.gui.mangadescription)

        self.gui.scrollwidget.setLayout(self.gui.scrollvbox)

        #Scroll Area Properties
        scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollarea.setWidgetResizable(True)
        scrollarea.setWidget(self.gui.scrollwidget)

        self.show()

        
        # print(tab.text())

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()