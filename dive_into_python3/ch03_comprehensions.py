#!/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import time
import humansize #自作ファイルを読み込み

print(os.getcwd()) # cwd = current working directory
os.chdir('C:\\')
print(os.getcwd()) # cwd = current working directory

os.chdir('C:\\Users')
print(os.getcwd()) # cwd = current working directory

# error
#os.chdir('C:\\nowhere')

path = os.path.join('/cygdrive/c', 'work')
print(path)

# ホームディレクトリ
print(os.path.expanduser('~'))

# ディレクトリとファイル名に分ける
(dirname, filename) = os.path.split(path)
print (dirname, filename)

# 拡張子とそれ以外に分ける
(shortname, extension) = os.path.splitext('something.txt')
print (shortname, extension)

# ファイル情報の取得
os.chdir(os.path.expanduser('~'))
metadata = os.stat('.zshrc')
print (metadata.st_mtime)  # ファイルの最終更新日
print (time.localtime(metadata.st_mtime)) # 読みやすく
print (metadata.st_size) # ファイルのサイズ
print (humansize.approximate_size(metadata.st_size)) # 読みやすく

# 絶対パスを取得
print (os.path.realpath('.zshrc'))

# リスト内包表記
a = [elem * 2 for elem in range(1, 100) if elem % 3 == 0]
print (a)

# 辞書内包表記
b = {str: len(str) for str in ["Monday", "Tuesday", "Wednesday"]}
print (b)
c = list(b.keys())
print (c)
b_reverse = {value: key for (key, value) in b.items()}
print (b_reverse)

# 集合内包表記
d = {item * 2 for item in range(1,10)}
print (d)

