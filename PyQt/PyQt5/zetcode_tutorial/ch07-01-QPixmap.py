#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we dispay an image
on the window. 

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, 
    QLabel, QApplication)
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        hbox = QHBoxLayout(self)

        # 画像が小さすぎて以下のエラーが出た
        # QWindowsWindow::setGeometryDp: Unable to set geometry 92x92+308+230 on QWidgetWindow/'ExampleClassWindow'. Resulting geometry:  116x92+308+230 (frame: 8, 30, 8, 8, custom margin: 0, 0, 0, 0, minimum size: 92x92, maximum size: 16777215x16777215).
        #pixmap = QPixmap("ch01-icon.png")

        # こちらはOK
        pixmap = QPixmap("board.jpg")

        # QLabelの上にpixmapを貼っている
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
