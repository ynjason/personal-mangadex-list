# personal-mangadex-list

Very basic personal manga list with readerfrom mangadex.\
Can keep track of currently reading, to try and completed manga.\
Gives basic description of manga with a list of chapters and picture of cover\
can add new manga into each list and move between lists\
Can update and download new chapters released to Mangadex and read them on a reader\
can keep track of where you read off on\
Maintains cover img and chapters from Mangadex

## Getting Started

* download this and run python main.py\
or
* You can also take the main.exe file and run it\
In order to use the app, go to [mangadex](https://mangadex.org/) and find a manga you want to keep track of. Copy and paste the title link into the text box labeled for manga urls. Go to the large drop down menu and select the manga you want displayed in the box and hit the select button. This shows information about the manga as well as a chapter list. Hit update all and download new to update for new chapters and downloading the updated chapters. Click the respective chapter in the chapter list to read the chapter. Downloaded chapters are displayed as blue in the chapter list.  While reading hit left and right arrows to move pages or use the drop down menu to jump between pages. Double click can also be used to move forward in pages if left and right do not work. When a chapter is marked as read or all the pages have been navigated through, when the menu button is clicked the read chapters will be deleted. A chapter can also be marked as unread to make it available to be downloaded again.

### Prerequisites
```
pip install pyqt5
pip install cloudscraper
```

## Built With

* [python](https://www.python.org/)
* [cloudscraper](https://pypi.org/project/cloudscraper/) - scraping
* [pyqt5](https://www.riverbankcomputing.com/software/pyqt/download5) - making gui
* [mangadex](https://mangadex.org/) - where to get manga

## Authors

* **Jason Ye** - *Initial work* - [Jason Ye](https://github.com/ynjason)


## Acknowledgments

Built based off of [mangadex-dl](https://github.com/frozenpandaman/mangadex-dl) by frozenpandaman