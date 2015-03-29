#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget,
                             QGridLayout, QHBoxLayout, QVBoxLayout,
                             QLabel, QLineEdit, QTextEdit,
                             QTableWidget,
                             QTableWidgetItem,
                             QPushButton, QApplication)
from PyQt5.QtCore import Qt
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# 形態素解析した結果をリストで返す
pageurl = "http://jlp.yahooapis.jp/MAService/V1/parse"
def morph(sentence, appid, results="ma", filter="1|2|3|4|5|6|7|8|9|10|11|12|13"):
    ret = []

    # 文章をURLエンコーディング
    sentence = urllib.parse.quote_plus(sentence.encode("utf-8"))
    query = "%s?appid=%s&results=%s&filter=%s&sentence=%s" % (pageurl, appid, results, filter, sentence)
    res = urllib.request.urlopen(query)

    soup = BeautifulSoup(res.read())
    # print(soup.prettify())
    return [(w.surface.string, w.reading.string, w.pos.string)
            for w in soup.ma_result.word_list]

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def buttonClicked(self):
        result = morph(self.text_lineedit.toPlainText(), appid=self.api_lineedit.text())

        ans = ""
        self.result_table.setRowCount( len(result) + 1 )
        for i, (word, reading, pos) in enumerate(result):
            self.result_table.setItem(i+1, 0, QTableWidgetItem(word))
            self.result_table.setItem(i+1, 1, QTableWidgetItem(reading))
            self.result_table.setItem(i+1, 2, QTableWidgetItem(pos))


    def initUI(self):

        api_label = QLabel("Yahoo API")
        self.api_lineedit = QLineEdit()
        hbox1 = QHBoxLayout()
        hbox1.addWidget(api_label)
        hbox1.addWidget(self.api_lineedit)

        text_label = QLabel("解析したい日本語")
        self.text_lineedit = QTextEdit()
        hbox2 = QHBoxLayout()
        hbox2.addWidget(text_label)
        hbox2.addWidget(self.text_lineedit)

        go_button = QPushButton("Go")
        go_button.clicked.connect(self.buttonClicked)
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(go_button)
        hbox3.addStretch(1)

        result_label = QLabel("解析結果")
        #self.result_lineedit = QTextEdit()
        #self.result_lineedit.setEnabled(False)
        self.result_table = QTableWidget()
        self.result_table.setColumnCount(3)
        self.result_table.setRowCount(1)
        self.result_table.setItem(0, 0, QTableWidgetItem("表記"))
        self.result_table.setItem(0, 1, QTableWidgetItem("読みがな"))
        self.result_table.setItem(0, 2, QTableWidgetItem("品詞"))
        hbox4 = QHBoxLayout()
        hbox4.addWidget(result_label)
        hbox4.addWidget(self.result_table)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 700, 550)
        self.setWindowTitle('Yahoo形態素解析のデモ')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ret = app.exec_()
    sys.exit(ret)
