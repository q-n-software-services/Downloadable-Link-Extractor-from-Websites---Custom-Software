# Importing built-in functions from libraries
from PyQt5.QtWidgets import QApplication, QDialog, QComboBox, QLineEdit, QFontComboBox, QVBoxLayout, QHBoxLayout, QDial, \
    QTextEdit, QLCDNumber, QMessageBox, QListWidget, QListWidgetItem, QListView, QPushButton, QCalendarWidget, QLabel, \
    QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
import sys
import re
import time

my_url = 'https://www.eidgahsharif.org/'
# my_url = 'https://wolf5th.blogspot.com/'

extracted_links = set()
done_links = set()
webpages = set()
webpages.add(my_url)
downloadable_links = []
anonymous_links = [my_url]

previous_link = ''

page = ''
soup = ''

# Below is the GUI code written using PyQt5 library of PYTHON
class Window(QWidget):
    def __init__(self):
        super().__init__()

        # self.showFullScreen()
        self.setGeometry(400, 100, 600, 300)

        self.setWindowTitle("Twitter Bot")
        self.setWindowIcon(QIcon("burger.ico"))

        self.create_combo_box()

    def create_combo_box(self):

        vbox = QVBoxLayout()

        vbox1 = QVBoxLayout()

        self.label = QLabel("Link Scraper")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Sanserif", 48))
        self.label.setFixedHeight(129)

        self.label.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:aqua; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        vbox.addWidget(self.label)

        self.link_title = QLabel()
        self.link_title.setAlignment(Qt.AlignCenter)
        self.link_title.setFont(QFont("Sanserif", 29))
        self.link_title.setText("Website URL")
        self.link_title.setStyleSheet("background-color:white")

        vbox1.addWidget(self.link_title)

        self.link = QLineEdit()
        self.link.setFont(QFont("Sanserif", 22))
        self.link.setPlaceholderText("\tEnter the LINK to the Website here")
        self.link.setStyleSheet("background-color:white")

        vbox1.addWidget(self.link)

        vbox.addLayout(vbox1)

        btn_points = QPushButton("SUBMIT")
        btn_points.setFont(QFont("sanserif", 16))
        btn_points.setStyleSheet("text-shadow: 1px 2px 2px #1C6EA4;background-color:lawngreen; border: 3px solid rgba(0,0,0,0.1); box-shadow:inset 0 1px 0 rgba(255,255,255,0.5),0 2px 2px rgba(0,0,0,0.3),0 0 4px 1px rgba(0,0,0,0.2),inset 0 3px 2px rgba(255,255,255,.22),inset 0 -3px 2px rgba(0,0,0,.15),inset 0 20px 10px rgba(255,255,255,.12),0 0 4px 1px rgba(0,0,0,.1),0 3px 2px rgba(0,0,0,.2);")
        btn_points.clicked.connect(self.submit_points)
        vbox.addWidget(btn_points)

        self.setLayout(vbox)

    def submit_points(self):
        # print('Clicked')
        self.webLink = self.link.text()
        if len(self.webLink) < 12:
            self.multi_choice_msgBox()
        if len(self.webLink) >= 12:
            my_func(self.webLink)

    def multi_choice_msgBox(self):
        message = QMessageBox.question(self, "Alert Message", f" Link Provided is quite small !\t Only {len(self.webLink)} characters. \nPlease Recheck it and press YES if you want to continue! ", QMessageBox.Yes |QMessageBox.No)

        if message == QMessageBox.Yes:
            my_func(self.webLink)
        elif message == QMessageBox.No:
            print("\n\nURL search Aborted Successfully\n\n")



# Main Code Starts Here
import datetime

from bs4 import BeautifulSoup
import requests


def handle_link(link):
    try:
        link = str(link)

        # print("link is : \t", link)

        global my_url
        global extracted_links
        global done_links
        global webpages
        global downloadable_links
        global anonymous_links
        global previous_link
        global page
        global soup

        extracted_links.add(link)

        if 'html' == link.split('.')[-1]:
            webpages.add(link)
        elif 'htm' == link.split('.')[-1]:
            webpages.add(link)
        elif 'xml' == link.split('.')[-1]:
            webpages.add(link)
        elif 'https://mega.nz' in link:
            downloadable_links.append(link)
        elif 'jpg' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'jpeg' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'png' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'svg' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'gif' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'giff' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'ico' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'tif' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'tiff' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'bmp' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'tga' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'iff' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'wbmp' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'psb' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'xbm' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'xpm' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'pdf' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'txt' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'doc' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'csv' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'xls' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'xlsx' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'json' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'zip' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'tsv' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'jfif' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'xpm' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'ppt' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'odt' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'exe' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'dmg' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'wav' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'mp3' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'wma' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'ogg' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'lpcm' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'bwf' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'aes3' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'dat' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'rf64' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'sln' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'mbwf' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'aac' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'flac' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'wma' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'pcm' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'aiff' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'alac' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'bin' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'gis' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'crf' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'img' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'dot' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'wbk' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'hfa' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'hdf' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'mp4' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'mp5' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'mpg' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'mpeg' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'mpeg4' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'mpeg5' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'kml' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'viv' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'ar' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'safe' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'mov' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'avi' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'avchd' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'flv' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'f4v' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'swf' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'mkv' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'webm' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'apk' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'bat' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'cgi' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'dif' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'diff' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'ifds' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'dat' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'odf' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'jp2' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'vcd' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'mpp' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'mpx' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'psd' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'step' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'fld' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'ldt' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'xlw' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'dvi' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'egt' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'tlf' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'dll' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'dol' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'xcf' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'gimp' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'vhd' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'woff' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'wtv' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'dxf' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'dwg' == link.split('.')[-1]:
            downloadable_links.append(link)
        elif 'rar' == link.split('.')[-1]:
            downloadable_links.append(link)
        else:
            webpages.add(link)
    except:
        print("Problem in Handle Link Funtion for :\t", link)


def a_tags(base_url):
    global file
    global my_url
    global extracted_links
    global done_links
    global webpages
    global downloadable_links
    global anonymous_links
    global previous_link
    global page
    global soup

    try:
        links = soup.find_all('a')
        print('Total "a" tags are : \t', len(links))
        # print(links)

        if 'asp' in base_url.split('.')[-1]:
            base_url = base_url.split('/')
            a = base_url.pop()
            base_url = '/'.join(base_url)

        for i, link in enumerate(links):
            try:
                # print(i + 1, link['href'])
                # file.write(f"{link['href']}\n")
                if 'http://' in link['href'] or 'https://' in link['href']:
                    url = link['href']
                elif '//' in link['src']:
                    url = 'https:' + link['src']
                else:
                    url = base_url + '/' + link['href']

                handle_link(url)
            except:
                print(i + 1, 'ERROR! "a" tag')
    except:
        print("Error in a_tags for \t", base_url)


def video_tags(base_url):
    global file
    global my_url
    global extracted_links
    global done_links
    global webpages
    global downloadable_links
    global anonymous_links
    global previous_link
    global page
    global soup

    try:
        links = soup.find_all('source')
        # print(len(links))
        # print(links)

        print('Total "source/picture/video" tags are : \t', len(links))

        if 'asp' in base_url.split('.')[-1]:
            base_url = base_url.split('/')
            a = base_url.pop()
            base_url = '/'.join(base_url)

        for i, link in enumerate(links):
            try:
                # print(i + 1, link['srcset'])

                if 'http://' in link['src'] or 'https://' in link['src']:
                    url = link['src']
                elif '//' in link['src']:
                    url = 'https:' + link['src']
                else:
                    url = base_url + '/' + link['src']

                print(i + 1, url)

                handle_link(url)

            except:
                print(i + 1, 'ERROR! "video" tag')
    except:
        print("Error in video_tags for \t", base_url)


def picture_tags(base_url):
    global file
    global my_url
    global extracted_links
    global done_links
    global webpages
    global downloadable_links
    global anonymous_links
    global previous_link
    global page
    global soup

    try:
        links = soup.find_all('source')
        # print(len(links))
        # print(links)

        print('Total "source/picture/video" tags are : \t', len(links))

        if 'asp' in base_url.split('.')[-1]:
            base_url = base_url.split('/')
            a = base_url.pop()
            base_url = '/'.join(base_url)

        for i, link in enumerate(links):
            try:
                # print(i + 1, link['srcset'])

                if 'http://' in link['srcset'] or 'https://' in link['srcset']:
                    url = link['srcset']
                elif '//' in link['srcset']:
                    url = 'https:' + link['srcset']
                else:
                    url = base_url + '/' + link['srcset']

                print(i + 1, url)

                handle_link(url)

            except:
                print(i + 1, 'ERROR! "picture" tag')
    except:
        print("Error in picture_tags for \t", base_url)


def area_tags(base_url):
    global file
    global my_url
    global extracted_links
    global done_links
    global webpages
    global downloadable_links
    global anonymous_links
    global previous_link
    global page
    global soup

    try:
        links = soup.find_all('area')
        # print(len(links))
        # print(links)

        if 'asp' in base_url.split('.')[-1]:
            base_url = base_url.split('/')
            a = base_url.pop()
            base_url = '/'.join(base_url)

        print('Total "map/area" tags are : \t', len(links))

        for i, link in enumerate(links):
            try:
                # print(i + 1, link['href'])

                if 'http://' in link['href'] or 'https://' in link['href']:
                    url = link['href']
                elif '//' in link['href']:
                    url = 'https:' + link['href']
                else:
                    url = base_url + '/' + link['href']

                print(i + 1, url)

                handle_link(url)

            except:
                print(i + 1, 'ERROR! "area" tag')
    except:
        print("Error in area_tags for \t", base_url)


def audio_tags(base_url):
    global file
    global my_url
    global extracted_links
    global done_links
    global webpages
    global downloadable_links
    global anonymous_links
    global previous_link
    global page
    global soup

    try:
        links = soup.find_all('audio')
        # print(len(links))
        # print(links)

        if 'asp' in base_url.split('.')[-1]:
            base_url = base_url.split('/')
            a = base_url.pop()
            base_url = '/'.join(base_url)

        print('Total "audio" tags are : \t', len(links))

        for i, link in enumerate(links):
            try:
                # print(i + 1, link['src'])

                if 'http://' in link['src'] or 'https://' in link['src']:
                    url = link['src']
                elif '//' in link['src']:
                    url = 'https:' + link['src']
                else:
                    url = base_url + '/' + link['src']

                print(i + 1, url)

                handle_link(url)

            except:
                print(i + 1, 'ERROR! "audio" tag')
    except:
        print("Error in audio_tags for \t", base_url)


def img_tags(base_url):
    global file
    global my_url
    global extracted_links
    global done_links
    global webpages
    global downloadable_links
    global anonymous_links
    global previous_link
    global page
    global soup

    try:
        links = soup.find_all('img')
        # print(len(links))
        # print(links)

        if 'asp' in base_url.split('.')[-1]:
            base_url = base_url.split('/')
            a = base_url.pop()
            base_url = '/'.join(base_url)

        print('Total "img" tags are : \t', len(links))

        for i, link in enumerate(links):
            try:
                # print(i + 1, link['src'])

                if 'http://' in link['src'] or 'https://' in link['src']:
                    url = link['src']
                elif '//' in link['src']:
                    url = 'https:' + link['src']
                else:
                    url = base_url + '/' + link['src']

                # print(i + 1, url)

                handle_link(url)

            except:
                print(i + 1, 'ERROR! "img" tag')
    except:
        print("Error in img_tags for \t", base_url)


def regex_scraper(base_url, this_page):
    global file
    global my_url
    global extracted_links
    global done_links
    global webpages
    global downloadable_links
    global anonymous_links
    global previous_link
    global page
    global soup

    newList = re.findall(r'https://\S+', str(this_page))
    newList = [str(item).replace('"', '') for item in newList]
    newList = [str(item).split('<')[0] for item in newList]
    newList = [str(item).split('>')[0] for item in newList]
    newList = [str(item).split(',')[0] for item in newList]

    for link in newList:
        handle_link(link)


def my_func(inputLink):
    # print("You Just clicked the button Successfully")
    # a, img, article, audio, iframe, map, picture, source, svg, video, xml file type
    global my_url
    global extracted_links
    global done_links
    global webpages
    global downloadable_links
    global anonymous_links
    global previous_link
    global page
    global soup


    required_types = [
        'application/EDIFACT', 'application/ogg', 'application/pdf', 'application/x-shockwave-flash', 'application/json',
        'application/ld+json', 'application/zip', 'audio/mpeg', 'audio/x-ms-wma', 'audio/vnd.rn-realaudio',
        'audio/x-wav', 'image/gif', 'image/jpeg', 'image/png', 'image/tiff', 'image/vnd.microsoft.icon', 'image/x-icon',
        'image/vnd.djvu', 'image/svg+xml', 'text/csv', 'video/mpeg', 'video/mp4', 'video/quicktime', 'video/x-ms-wmv',
        'video/x-msvideo', 'video/x-flv', 'video/webm', 'VND	application/vnd.oasis.opendocument.text',
        'application/vnd.oasis.opendocument.spreadsheet', 'application/vnd.oasis.opendocument.presentation',
        'application/vnd.oasis.opendocument.graphics', 'application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        'application/vnd.ms-powerpoint', 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    ]

    my_url = inputLink.strip()

    # my_url = 'https://www.eidgahsharif.org/'
    # my_url = 'https://wolf5th.blogspot.com/'

    extracted_links = set()
    done_links = set()
    webpages = set()
    webpages.add(my_url)
    downloadable_links = []
    anonymous_links = [my_url]

    previous_link = ''
    # Recursion Part

    while len(webpages) > 0 or len(anonymous_links) > 0:
        try:
            webpages = list(webpages)
            dump = webpages.pop()
            webpages = set(webpages)
        except:
            pass

        try:
            dump2 = anonymous_links.pop()
        except:
            pass
        print(f'\n\n\n{my_url}\n\n\n')
        if my_url == previous_link:
            break

        if 'www.youtube.com' in my_url:
            continue

        if 'https://mega.nz' in my_url:
            extracted_links.add(my_url)
            downloadable_links.append(my_url)
            done_links.add(my_url)
            continue

        if 'http://anonym.to' in my_url:
            continue

        try:
            page = requests.get(my_url)
            soup = BeautifulSoup(page.content, 'html.parser')
        except:
            continue

        contentType = 'None'
        try:
            if ';' in page.headers['Content-Type']:
                contentType = page.headers['Content-Type'].split(';')[0]
            else:
                contentType = page.headers['Content-Type']
        except:
            print("This Page is erroneous :\t", my_url)
            continue

        if contentType in required_types:
            extracted_links.add(my_url)
            downloadable_links.append(my_url)
        else:
            regex_scraper(my_url, str(soup))
            a_tags(my_url)
            img_tags(my_url)
            audio_tags(my_url)
            area_tags(my_url)
            picture_tags(my_url)
            video_tags(my_url)

        done_links.add(my_url)
        previous_link = my_url

        try:
            webpages = list(webpages)
            my_url = webpages.pop(0)
            webpages = set(webpages)
        except:
            try:
                my_url = anonymous_links.pop(0)
            except:
                print("Only ! link available")
                downloadable_links.append(previous_link)
        while my_url in done_links:
            print(my_url)
            webpages = list(webpages)
            if len(webpages) > 0:
                my_url = webpages.pop(0)
                webpages = set(webpages)
            elif len(anonymous_links) > 0:
                my_url = anonymous_links.pop(0)
            else:
                webpages = set(webpages)
                break

    # At very End
    now = datetime.datetime.now()
    now = '_'.join(str(now).split())
    now = '.'.join(str(now).split(':'))

    downloadable_links = set(downloadable_links)
    downloadable_links = list(downloadable_links)

    file = open(f"extracted_links_{now}.txt", 'a')
    for link in downloadable_links:
        file.write(f'{link}\n')
    file.close()

    print("\n\n\n")
    print("Total Links Extracted are : \t", len(extracted_links))
    print("Total Webpages are : \t", len(webpages))
    print("Total Downloadable Links are : \t", len(downloadable_links))
    # print("Total Anonymous Links are : \t", len(anonymous_links))

    # file = open(f"anonymous_{now}.txt", 'a')
    # for link in anonymous_links:
    #     file.write(f'{link}\n')
    # file.close()

    file = open(f"all_links_{now}.txt", 'a')
    for link in extracted_links:
        file.write(f'{link}\n')
    file.close()


# GUI window setup clauses

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())








