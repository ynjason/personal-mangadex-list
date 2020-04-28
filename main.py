from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from download import float_conversion, zpad, download_specific_manga
from update import update_all_mangas
from gui import Ui_gui
from reader import Ui_reader
import cloudscraper
import time, os, sys, re, json, html, copy, shutil
import sys
import functools

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
        # print(r)
        manga = json.loads(r.text)
        print(manga)
    except (json.decoder.JSONDecodeError, ValueError) as err:
        print("CloudFlare error: {}".format(err))
        return []

    # check available chapters
    chapters = []

    if "chapter" not in manga:
        print("Chapter not found in the language you requested.")
        return []

    for chap in manga["chapter"]:
        if manga["chapter"][str(chap)]["lang_code"] == "gb":
            chapters.append(manga["chapter"][str(chap)]["chapter"])
    chapters.sort(key=float_conversion) # sort numerically by chapter #

    chapters_revised = ["Oneshot" if x == "" else x for x in chapters]

    chaps_to_show = []
    print(chapters)
    for chapter_id in manga["chapter"]:
        try:
            chapter_num = str(float(manga["chapter"][str(chapter_id)]["chapter"])).replace(".0","")
        except:
            chapter_num = ''
            pass # Oneshot
        chapter_group = manga["chapter"][chapter_id]["group_name"]
        if chapter_num in chapters and manga["chapter"][chapter_id]["lang_code"] == "gb":
            if chapter_num != '':
                chaptername = "c{} [{}]".format(zpad(chapter_num), chapter_group)
                chaps_to_show.append((str(chapter_num), chaptername))
            else:
                chaptername = "c{} [{}]".format(zpad(str(0)), chapter_group)
                chaps_to_show.append((str(0), chaptername))
    chaps_to_show.sort(key=lambda x: float(x[0]))

    if len(chaps_to_show) == 0:
        print("No chapters available!")
        return []
    return chaps_to_show

class Main(QMainWindow):
    def get_mangaid(self, title, tab):
        for manga in self.profile[tab]:
            if manga['title'] == title:
                return manga['title_id']


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

        self.gui.download_btn_grp = QtWidgets.QButtonGroup()
        self.gui.download_btn_grp.setExclusive(True)
        self.gui.download_btn_grp.addButton(self.gui.downloadnew_1)
        self.gui.download_btn_grp.addButton(self.gui.downloadnew_2)
        self.gui.download_btn_grp.addButton(self.gui.downloadnew_3)
        self.gui.download_btn_grp.buttonClicked.connect(self.handle_download_click)

        self.gui.update_btn_grp = QtWidgets.QButtonGroup()
        self.gui.update_btn_grp.setExclusive(True)
        self.gui.update_btn_grp.addButton(self.gui.updateall_1)
        self.gui.update_btn_grp.addButton(self.gui.updateall_2)
        self.gui.update_btn_grp.addButton(self.gui.updateall_3)
        self.gui.update_btn_grp.buttonClicked.connect(self.handle_update_click)

        self.gui.move_btn_grp = QtWidgets.QButtonGroup()
        self.gui.move_btn_grp.setExclusive(True)
        self.gui.move_btn_grp.addButton(self.gui.confirmmove_1)
        self.gui.move_btn_grp.addButton(self.gui.confirmmove_2)
        self.gui.move_btn_grp.addButton(self.gui.confirmmove_3)
        self.gui.move_btn_grp.buttonClicked.connect(self.handle_move_click)

        self.gui.url_1.returnPressed.connect(lambda: self.handle_url_submit(self.gui.url_1))
        self.gui.url_2.returnPressed.connect(lambda: self.handle_url_submit(self.gui.url_2))
        self.gui.url_3.returnPressed.connect(lambda: self.handle_url_submit(self.gui.url_3))

        self.gui.remove_btn_grp = QtWidgets.QButtonGroup()
        self.gui.remove_btn_grp.setExclusive(True)
        self.gui.remove_btn_grp.addButton(self.gui.Remove_1)
        self.gui.remove_btn_grp.addButton(self.gui.Remove_2)
        self.gui.remove_btn_grp.addButton(self.gui.Remove_3)
        self.gui.remove_btn_grp.buttonClicked.connect(self.handle_remove_click)

        self.updated_manga = {}
        self.to_download = {}
    
    def handle_url_submit(self, lineedit):
        tabindex = self.gui.tabWidget.currentIndex()
        url = lineedit.text()
        print(url)
        try:
            manga_id = re.search("[0-9]+", url).group(0)
            split_url = url.split("/")
            for segment in split_url:
                if "mangadex" in segment:
                    url = segment.split('.')
                    tld = url[1]
        except:
            print("Error with URL.")
        scraper = cloudscraper.create_scraper()
        try:
            r = scraper.get("https://mangadex.{}/api/manga/{}/".format(tld, manga_id))
            manga = json.loads(r.text)
            print(manga)
        except (json.decoder.JSONDecodeError, ValueError) as err:
            print("CloudFlare error: {}".format(err))
            exit(1)

        try:
            title = manga["manga"]["title"]
        except:
            print("Please enter a MangaDex manga (not chapter) URL.")
            exit(1)

        new = {
                "title": title,
                "title_id": manga_id,
                "description": manga["manga"]["description"],
                "author": manga["manga"]["author"],
                "artist": manga["manga"]["artist"],
                "url": "https://mangadex.{}/api/manga/{}/".format(tld, manga_id),
                "cover_url": "https://mangadex.{}".format(tld+manga["manga"]["cover_url"]),
                "recent_read": 0,
                "recent_update": 0,
                "new_update": [],
                "tld": tld
                }
        self.profile[tabindex].append(new)
        with open('profile.json', 'w+') as outfile:
            json.dump(self.profile, outfile)

        findcombo = "Mangaselect_" + str(tabindex+1)
        findcombomove = "manga_" + str(tabindex+1)

        combobox = self.gui.tabWidget.findChild(QtWidgets.QComboBox, findcombo)
        comboboxmove = self.gui.tabWidget.findChild(QtWidgets.QComboBox, findcombomove)
        for combox in [combobox, comboboxmove]:
            combox.addItem(title)

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
        if findmanga == '':
            return
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

        self.gui.mangadescription = QtWidgets.QLabel(manga['description'])
        self.gui.scrollvbox.addWidget(self.gui.mangadescription)

        self.gui.mangaauthor = QtWidgets.QLabel("author: " + manga['author'])
        self.gui.scrollvbox.addWidget(self.gui.mangaauthor)

        self.gui.mangaartist = QtWidgets.QLabel("artist: " + manga['artist'])
        self.gui.scrollvbox.addWidget(self.gui.mangaartist)

        self.gui.mangaread = QtWidgets.QLabel("recently read chapter: " + str(manga['recent_read']))
        self.gui.scrollvbox.addWidget(self.gui.mangaread)

        newupdate = "New Updates: "
        if len(manga['new_update']) == 0:
            newupdate += "None"
        else:
            for chapter in manga['new_update']:
                if chapter == '':
                    newupdate += 'Oneshot '
                else:
                    newupdate += str(chapter) + ' '
        self.gui.newupdate = QtWidgets.QLabel(newupdate)
        self.gui.scrollvbox.addWidget(self.gui.newupdate)

        chapters = getchapterlist(manga)
        downloaded_list = []
        for chapter in chapters:
            dest_folder = os.path.join(os.getcwd(), "download", manga['title'], chapter[1])
            if os.path.isdir(dest_folder):
                downloaded_list.append(chapter[1])
    
        # self.gui.chapterbtn_grp = QtWidgets.QButtonGroup()
        # self.gui.chapterbtn_grp.setExclusive(True)
        # self.gui.chapterbtn_grp.buttonClicked.connect(lambda: self.gotoreader(tabindex, manga['title'], downloaded_list))
        counter = 0
        for i, chapter in enumerate(chapters):
            dest_folder = os.path.join(os.getcwd(), "download", manga['title'], chapter[1])
            if os.path.isdir(dest_folder):
                # object = QtWidgets.QPushButton()
                # object.setObjectName(chapter[1])
                # object.setAlignment(QtCore.Qt.AlignLeft)
                # object.setText(chapter[1])
                object = QLabel(chapter[1])
                # object.clicked.connect(lambda: self.gotoreader(tabindex, manga['title'], downloaded_list, counter))
                object.mousePressEvent = functools.partial(self.gotoreader, category=tabindex, manga=manga['title'], chapter_list=downloaded_list, chapter_index=counter)
                # self.gui.chapterbtn_grp.addButton(object)
                counter += 1
                self.gui.scrollvbox.addWidget(object)
            else:
                object = QLabel(chapter[1])
                self.gui.scrollvbox.addWidget(object)
        self.gui.scrollwidget.setLayout(self.gui.scrollvbox)

        #Scroll Area Properties
        scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollarea.setWidgetResizable(True)
        scrollarea.setWidget(self.gui.scrollwidget)

        self.show()
    
    def gotoreader(self, event, category, manga, chapter_list, chapter_index):
        # print(btn.text())
        print(chapter_index)
        print(chapter_list)
        self.reader = Reader(category, manga, chapter_list, chapter_index)
        self.reader.show()
        self.close()

    def handle_download_click(self, btn):
        tabindex = self.gui.tabWidget.currentIndex()
        for title, new_chapters in self.to_download.items():
            mangaid = self.get_mangaid(title, tabindex)
            download_specific_manga(mangaid, new_chapters)

    def handle_move_click(self, btn):
        tabindex = self.gui.tabWidget.currentIndex()
        findcombo = "manga_" + str(tabindex+1)
        selectcombo = self.gui.tabWidget.findChild(QtWidgets.QComboBox, findcombo)
        findmanga = selectcombo.currentText()
        print(findmanga)
        selectcombo.removeItem(selectcombo.currentIndex())

        remove_manga = "Mangaselect_" + str(tabindex+1)
        mangacombo = self.gui.tabWidget.findChild(QtWidgets.QComboBox, remove_manga)
        mangacombo.removeItem(mangacombo.findText(findmanga, QtCore.Qt.MatchFixedString))

        new_tab = "category_" + str(tabindex+1)
        tagcombo = self.gui.tabWidget.findChild(QtWidgets.QComboBox, new_tab)
        category = tagcombo.currentText()

        if category == "Currently Reading":
            self.gui.tabWidget.setCurrentIndex(0)

        elif category == "To Try":
            self.gui.tabWidget.setCurrentIndex(1)

        else:
            self.gui.tabWidget.setCurrentIndex(2)

        tabindex2 = self.gui.tabWidget.currentIndex()
        findcombo = "manga_" + str(tabindex2+1)
        selectcombo = self.gui.tabWidget.findChild(QtWidgets.QComboBox, findcombo)
        selectcombo.addItem(findmanga)

        remove_manga = "Mangaselect_" + str(tabindex2+1)
        mangacombo = self.gui.tabWidget.findChild(QtWidgets.QComboBox, remove_manga)
        mangacombo.addItem(findmanga)

        self.gui.tabWidget.setCurrentIndex(tabindex)

        for i, manga in enumerate(self.profile[tabindex]):
            if manga['title'] == findmanga:
                removed_manga = self.profile[tabindex].pop(i)
        self.profile[tabindex2].append(removed_manga)
        with open('profile.json', 'w+') as outfile:
            json.dump(self.profile, outfile)


    def handle_update_click(self, btn):
        tabindex = self.gui.tabWidget.currentIndex()
        for manga in self.profile[tabindex]:
            self.updated_manga[manga['title']] = []
            self.to_download[manga['title']] = []
        self.updated_manga, self.to_download = update_all_mangas(tabindex)
        with open('profile.json', 'r') as infile:
            self.profile = json.load(infile)
        print(self.updated_manga)


    def handle_remove_click(self, btn):
        tabindex = self.gui.tabWidget.currentIndex()
        findcombo = "Mangaselect_" + str(tabindex+1)
        selectcombo = self.gui.tabWidget.findChild(QtWidgets.QComboBox, findcombo)
        findmanga = selectcombo.currentText()
        if findmanga == '':
            return

        findcombo = "manga_" + str(tabindex+1)
        selectcombo = self.gui.tabWidget.findChild(QtWidgets.QComboBox, findcombo)
        selectcombo.removeItem(selectcombo.findText(findmanga, QtCore.Qt.MatchFixedString))

        remove_manga = "Mangaselect_" + str(tabindex+1)
        mangacombo = self.gui.tabWidget.findChild(QtWidgets.QComboBox, remove_manga)
        mangacombo.removeItem(mangacombo.findText(findmanga, QtCore.Qt.MatchFixedString))

        for i, manga in enumerate(self.profile[tabindex]):
            if manga['title'] == findmanga:
                removed_manga = self.profile[tabindex].pop(i)
        with open('profile.json', 'w+') as outfile:
            json.dump(self.profile, outfile)



class Reader(QMainWindow):
    def populate_combo_box(self):
        combobox = self.reader.centralwidget.findChild(QtWidgets.QComboBox, 'pagelist')
        combobox.clear()
        path = 'download/{}/{}/'.format(self.manga, self.chapter_list[self.chapter_index])
        pages = os.listdir(path)
        self.page_list = pages
        for page in pages:
            combobox.addItem(page.split('.')[0])


    def set_page_new_chap(self):
        path = 'download/{}/{}/'.format(self.manga, self.chapter_list[self.chapter_index])
        pages = os.listdir(path)
        self.page_list = pages
        self.page_index = 0


    def __init__(self, category, manga, chapter_list, chapter_index):
        QMainWindow.__init__(self)
        with open('profile.json', 'r') as infile:
            print("here")
            self.profile = json.load(infile)
        self.category = category
        self.chapter_list = chapter_list
        self.manga = manga
        self.chapter_index = chapter_index
        self.page_list = []
        self.page_index = 0
        self.reader = Ui_reader()
        self.reader.setupUi(self)
        self.populate_combo_box()
        self.setpage()
        self.read_chapters = []

        self.reader.jump.clicked.connect(self.handle_jump_click)
        self.reader.unread.clicked.connect(self.handle_unread_click)
        self.reader.read.clicked.connect(self.handle_read_click)
        self.reader.next.clicked.connect(self.handle_next_click)
        self.reader.previous.clicked.connect(self.handle_prev_click)
        self.reader.home.clicked.connect(self.handle_home_click)
        # left and right arrows

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Left:
            self.handle_left()
        elif event.key() == QtCore.Qt.Key_Right:
            self.handle_right()
        event.accept()

    def handle_left(self):
        if self.page_index > 0:
            self.page_index -= 1
            self.setpage()
        elif self.page_index == 0:
            self.handle_prev_click()

    def handle_right(self):
        if self.page_index < len(self.page_list)-1:
            self.page_index += 1
            self.setpage()
        elif self.page_index == len(self.page_list)-1:
            self.read_chapters.append(self.chapter_index)
            self.handle_next_click()

    def handle_jump_click(self):
        dest_page = self.reader.pagelist.currentIndex()
        self.page_index = dest_page
        self.setpage()

    def handle_unread_click(self):
        chapter = self.chapter_list[self.chapter_index]
        numchap = float(chapter.split(' ')[0][1:])
        for index, manga in enumerate(self.profile[self.category]):
            if manga['title'] == self.manga:
                self.profile[self.category][index]['recent_read'] = numchap-1
        with open('profile.json', 'w+') as outfile:
            json.dump(self.profile, outfile)
    
    def handle_read_click(self):
        chapter = self.chapter_list[self.chapter_index]
        numchap = float(chapter.split(' ')[0][1:])
        for index, manga in enumerate(self.profile[self.category]):
            if manga['title'] == self.manga:
                self.profile[self.category][index]['recent_read'] = numchap
        with open('profile.json', 'w+') as outfile:
            json.dump(self.profile, outfile)
        self.read_chapters.append(self.chapter_list[self.chapter_index])
        if self.chapter_index < len(self.chapter_list)-1:
            self.chapter_index += 1
            self.set_page_new_chap()
            self.setpage()

    def handle_next_click(self):
        if self.chapter_index < len(self.chapter_list)-1:
            self.chapter_index += 1
            self.set_page_new_chap()
            self.setpage()
    
    def handle_prev_click(self):
        if self.chapter_index > 0:
            self.chapter_index -= 1
            self.set_page_new_chap()
            self.setpage()

    def handle_home_click(self):
        # delete read chapters
        for chapter in self.read_chapters:
            path = "download/{}/{}/".format(self.manga, chapter)
            shutil.rmtree(path)
        self.main = Main()
        self.main.show()
        self.close()


    def setpage(self):
        scrollarea = self.reader.centralwidget.findChild(QtWidgets.QScrollArea, 'scrollArea')
        combobox = self.reader.centralwidget.findChild(QtWidgets.QComboBox, 'pagelist')

        combobox.setCurrentIndex(self.page_index)

        self.reader.scrollwidget = QWidget(scrollarea)
        self.reader.scrollvbox = QVBoxLayout(self.reader.scrollwidget)

        description = '{} page:{}'.format(self.chapter_list[self.chapter_index], self.page_list[self.page_index])
        object = QLabel(description)
        self.reader.scrollvbox.addWidget(object)
            
        self.reader.img = QtGui.QPixmap("download/{}/{}/{}".format(self.manga, self.chapter_list[self.chapter_index], self.page_list[self.page_index]))
        self.reader.img = self.reader.img.scaledToHeight(1024)
        self.reader.imglabel = QtWidgets.QLabel()
        self.reader.imglabel.setPixmap(self.reader.img)
        self.reader.scrollvbox.addWidget(self.reader.imglabel)

        self.reader.scrollwidget.setLayout(self.reader.scrollvbox)

        #Scroll Area Properties
        scrollarea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollarea.setWidgetResizable(True)
        scrollarea.setWidget(self.reader.scrollwidget)
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()