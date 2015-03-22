#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows an icon
in the titlebar of the window.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


# OOPスタイル
# QWidgetクラスを継承したクラスを作成
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        # QWidgetから継承した関数を呼んでいる
        self.setGeometry(300, 300, 300, 220)  # ウィンドウの場所とサイズを設定
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('ch01-icon.png'))        
    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
