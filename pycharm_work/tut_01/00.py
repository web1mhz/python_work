

# #main_content > div > ul > li > dl > dt > a

import sys, requests
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QDesktopServices as qd
from PyQt5.QtCore import QDate, QUrl
from bs4 import BeautifulSoup as bs, element

class main(QWidget):
    def __init__(self):
        super().__init__()

        self.qf = QFrame(self)
        self.btn1 = QPushButton('모바일', self)

