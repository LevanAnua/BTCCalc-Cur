import requests
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QPlainTextEdit, QPushButton
from bs4 import BeautifulSoup
from PyQt6.QtCore import *
from PyQt6 import QtWidgets
import sys


class Windows(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(900, 500)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 80, 131, 30))
        font = QFont()
        font.setFamilies([u"Jokerman"])
        font.setPointSize(19)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 80, 131, 30))
        font1 = QFont()
        font1.setFamilies([u"Jokerman"])
        font1.setPointSize(19)
        font1.setBold(False)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(560, 80, 131, 30))
        self.label_3.setFont(font)
        self.plainTextEdit = QPlainTextEdit(self)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(480, 180, 131, 36))
        font2 = QFont()
        font2.setFamilies([u"Jokerman"])
        font2.setPointSize(12)
        self.plainTextEdit.setFont(font2)
        self.pushButton = QPushButton(self)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(350, 380, 191, 51))
        self.pushButton.setFont(font1)
        self.label_5 = QLabel(self)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(260, 180, 161, 36))
        self.label_5.setFont(font)
        self.label_4 = QLabel(self)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(710, 80, 111, 30))
        self.label_4.setFont(font1)
        self.label_6 = QLabel(self)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 280, 191, 51))
        font3 = QFont()
        font3.setFamilies([u"Jokerman"])
        font3.setPointSize(19)
        font3.setKerning(True)
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.label.setText('BTC/USD')
        self.label_2.setText(str(ccurr.getcurr))
        self.label_3.setText('USD/RUB')
        self.label_4.setText(str(ccurr.getrub))
        self.label_5.setText('BTC Balance')
        self.pushButton.setText('Update')
        self.plainTextEdit.setPlainText('1')
        self.label_6.setText(str(int(float(ccurr.getcurr)
                                     * float(ccurr.getrub)
                                     * float(self.plainTextEdit.toPlainText())))
                             + '  RUB')

    def clicker(self):
        self.label_2.setText(str(ccurr.getcurr))
        balance = self.plainTextEdit.toPlainText().replace(",", ".")
        self.label_6.setText(str(int(float(ccurr.getcurr)
                                     * float(ccurr.getrub)
                                     * float(balance)))
                             + '  RUB')


class Currency:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/95.0.4638.69 Safari/537.36'}
    btcusdbinance = 'https://www.investing.com/crypto/bitcoin/btc-usd'
    usdrub = 'https://www.investing.com/currencies/usd-rub'

    curr = 0

    @property
    def getcurr(self):
        full_page = requests.get(self.btcusdbinance, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'lxml')
        convertbinance = soup.find_all('span', {'data-test': 'instrument-price-last'})
        final = str(convertbinance[0].text)
        konec = final.replace(",", "")
        return konec

    @property
    def getrub(self):
        full_page = requests.get(self.usdrub, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'lxml')
        rub = soup.find_all('span', {'data-test': 'instrument-price-last'}, {'class': "text-base"})
        final = str(rub[0].text)
        konec = final.replace(",", "")
        return konec


ccurr = Currency()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Windows()
    window.pushButton.clicked.connect(window.clicker)
    window.show()
    app.exec()


main()
