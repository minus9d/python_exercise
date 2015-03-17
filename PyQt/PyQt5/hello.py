#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets  # for PyQt5

def on_click():
    print("Hello")

def print_state(state):
    if state == 0:
        print("Unchecked")
    else:
        print("Checked")

def main():
    # PyQt4
    # app = QtGui.QApplication(sys.argv)
    # main_window = QtGui.QMainWindow()
    # hello_button = QtGui.QPushButton("Hello!")
    # check_box = QtGui.QCheckBox("Check Box")

    # PyQt5
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    hello_button = QtWidgets.QPushButton("Hello!")
    check_box = QtWidgets.QCheckBox("Check Box")

    hello_button.clicked.connect(check_box.toggle)
    check_box.stateChanged.connect(print_state)

    main_window.setCentralWidget(hello_button)
    main_window.setCentralWidget(check_box)
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    main()
