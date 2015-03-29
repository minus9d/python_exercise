#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget,
                             QGridLayout, QHBoxLayout, QVBoxLayout,
                             QLabel, QLineEdit, QPlainTextEdit,
                             QTableWidget,
                             QTableWidgetItem,
                             QPushButton,
                             QMessageBox,
                             QApplication)

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

        # ユーザが入力した文字列を形態素解析
        try:
            result = morph(self.text_textedit.toPlainText(), appid=self.api_lineedit.text())
        except urllib.error.HTTPError:
            reply = QMessageBox.question(
                self,
                'Error',
                '形態素解析結果の取得に失敗しました。アプリケーションIDは正しくセットされていますか？',
                QMessageBox.Ok,
                QMessageBox.Ok
                )
            return

        # テーブルに結果を出力
        self.result_table.setRowCount( len(result) + 1 )
        for i, (word, reading, pos) in enumerate(result):
            self.result_table.setItem(i+1, 0, QTableWidgetItem(word))
            self.result_table.setItem(i+1, 1, QTableWidgetItem(reading))
            self.result_table.setItem(i+1, 2, QTableWidgetItem(pos))


    def initUI(self):

        api_label = QLabel("Yahoo! アプリケーションID")
        api_lineedit = QLineEdit()
        self.api_lineedit = api_lineedit

        text_label = QLabel("解析したい日本語")
        text_textedit = QPlainTextEdit()
        self.text_textedit = text_textedit

        grid = QGridLayout()
        grid.addWidget(api_label, 0, 0)
        grid.addWidget(api_lineedit, 0, 1)
        grid.addWidget(text_label, 1, 0)
        grid.addWidget(text_textedit, 1, 1)

        go_button = QPushButton("Go")
        go_button.clicked.connect(self.buttonClicked)
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(go_button)
        hbox1.addStretch(1)

        result_label = QLabel("解析結果")
        result_table = QTableWidget()
        result_table.setColumnCount(3)
        result_table.setRowCount(1)
        result_table.setItem(0, 0, QTableWidgetItem("表記"))
        result_table.setItem(0, 1, QTableWidgetItem("読みがな"))
        result_table.setItem(0, 2, QTableWidgetItem("品詞"))
        self.result_table = result_table
        hbox2 = QHBoxLayout()
        hbox2.addWidget(result_label)
        hbox2.addWidget(result_table)

        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        self.setLayout(vbox)

        self.setGeometry(100, 100, 700, 550)
        self.setWindowTitle('Yahoo! 形態素解析のデモ')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    ret = app.exec_()
    sys.exit(ret)
