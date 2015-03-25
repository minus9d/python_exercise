#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows a QProgressBar widget.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        # タイマー
        self.timer = QBasicTimer()
        self.step = 0
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()
        
        
    def timerEvent(self, e):
        # カウントが100に達すると終了
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
    
        # 呼ばれるたび1ずつ増やす
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        

    def doAction(self):
        """ボタンが押されると呼ばれる"""

        # タイマーが実行中ならタイマーを停止する
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        # タイマーが停止中ならタイマーを実行する
        else:
            # (timeout[ms], イベントの受取先)
            # timeoutで指定した時間間隔でシグナルが飛ぶ模様
            self.timer.start(1000, self)
            self.btn.setText('Stop')
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
