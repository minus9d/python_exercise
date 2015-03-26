#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QGridLayout, 
    QPushButton, QApplication)
from PyQt5.QtCore import Qt


def return_widget(idx):
    idx = idx % 2
    if idx == 0:
        return QSlider(Qt.Horizontal)
    elif idx == 1:
        return QSlider(Qt.Vertical)

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        # widgetを作る
        widgets = [ [None for j in range(10)] for i in range(10) ]
        for j in range(10):
            for i in range(10):
                widgets[j][i] = return_widget(i+j)

        # connectする
        H = 10
        W = 10
        for j in range(H):
            for i in range(W):
                if i == W-1:
                    i2 = 0
                    j2 = (j + 1) % W
                else:
                    i2 = i + 1
                    j2 = j
                widgets[j][i].valueChanged.connect(widgets[j2][i2].setValue)

        # gridに配置
        grid = QGridLayout()
        self.setLayout(grid)
        for j in range(H):
            for i in range(W):
                grid.addWidget(widgets[j][i], j, i)
                
        self.move(300, 150)
        self.setWindowTitle('Too Many Sliders')
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

