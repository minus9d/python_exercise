#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we select a color value
from the QColorDialog and change the background
color of a QFrame widget. 

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, 
    QColorDialog, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        # 初期色
        col = QColor(0, 0, 0) 

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)

        # ボタンを押すとダイアログが開く
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" 
            % col.name())
        self.frm.setGeometry(130, 22, 100, 100)            
        
        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()
        
        
    def showDialog(self):

        # ユーザに色を選ばせる
        col = QColorDialog.getColor()

        # OKボタンが押された時だけ有効な色が返る
        if col.isValid():
            # スタイルシートを使って色を変える
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % col.name())
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
