#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program centers a window 
on the screen. 

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.resize(250, 150)
        self.center()  # ウィンドウをスクリーンの中央に寄せる自作関数
        
        self.setWindowTitle('Center')    
        self.show()
        
        
    def center(self):
        
        qr = self.frameGeometry()  # メインウィンドウのジオメトリを取得
        cp = QDesktopWidget().availableGeometry().center()   # スクリーンの解像度をもとに、その中心点を得る
        qr.moveCenter(cp) # 矩形の中心をスクリーンの中心に合わせる
        self.move(qr.topLeft())   # ウィンドウの左上を、矩形の左上に合わせる

        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())  
