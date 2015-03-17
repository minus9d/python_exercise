#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

def on_click():
    print("Hello")

def print_state(state):
    if state == 0:
        print("Unchecked")
    else:
        print("Checked")

def main():
    app = QtGui.QApplication(sys.argv)
    main_window = QtGui.QMainWindow()
    hello_button = QtGui.QPushButton("Hello!")
    check_box = QtGui.QCheckBox("Check Box")

    hello_button.clicked.connect(check_box.toggle)
    check_box.stateChanged.connect(print_state)

    main_window.setCentralWidget(hello_button)
    main_window.setCentralWidget(check_box)
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()
