#!/usr/bin/env python3

import locale
import io
import gzip
import sys

# デフォルトの文字コードを取得
# e.g. 'UTF-8'
print(locale.getpreferredencoding())

# PythonではOSに関わらず/を使えばOK
a_file = open('./ch11_japanese.txt', encoding='utf-8')

# './ch11_japanese.txt'
print(a_file.name)
# 'utf-8'
print(a_file.encoding)
# 'r'
print(a_file.mode)

# EOFに達した後でもエラーにはならない
print(a_file.read())
print(a_file.read())
print(a_file.read())

# ファイルの特定のバイト位置に移動
print(a_file.seek(0))
# 5文字読み込む
print(a_file.read(5))
# 現在のバイト位置
print(a_file.tell())


# ファイルが閉じられたことを確認
print(a_file.closed)
a_file.close()
print(a_file.closed)


# ファイルを自動的に閉じるテクニック
# (withにより実行時コンテクストを生成する)
with open('./ch11_japanese.txt', encoding='utf-8') as a_file:
    a_file.seek(15)
    a_character = a_file.read(1)
    print(a_character)

line_number = 0
with open('./ch11_japanese.txt', encoding='utf-8') as a_file:
    for a_line in a_file:
        line_number += 1
        # >4: 4文字分のスペースに右詰め
        print('{:>4} {}'.format(line_number, a_line.rstrip()))


# ファイル書き込み
with open('./write_test.txt', encoding='utf-8', mode='w') as a_file:
    # 改行はされないので注意
    a_file.write('国境の長いトンネルを抜けると雪国であった。')
    a_file.write('夜の底が白くなった。')

# バイナリの読み込み
with open('./ch11_image.png', mode='rb') as a_image:
    data = a_image.read(10)
    # b'\x89PNG\r\n\x1a\n\x00\x00'
    print(data)
    # <class 'bytes'>
    print(type(data))
    data = a_image.read()

    # ファイルサイズを表示
    a_image.seek(0)
    data = a_image.read()
    print(len(data))

# 擬似ファイルからの読み込み
a_string = '吾輩は猫である'
with io.StringIO(a_string) as a_file:
    print(a_file.read())
    a_file.seek(0)
    print(len(a_file.read()))


# gzipの読み書きも可能らしいがうまく動かない
# 文字コードの指定は4.3から可能らしい
# http://stackoverflow.com/questions/1883604/reading-utf-8-characters-from-a-gzip-file-in-python
# with gzip.open('ch11_japanese.txt.gz', mode = 'wb) as z_file:
    #z_file.write('この書生というのは時々我々を捕えて煮て食うという話である。')


# stdio
for i in range(3):
    # 改行なし
    sys.stdout.write('word')
    

# __enter__()と__exit__()を定義することでコンテクストマネージャになれてwithが使える
class RedirectStdoutTo:
    def __init__(self, out_new):
        self.out_new = out_new
    def __enter__(self):
        self.out_old = sys.stdout
        sys.stdout = self.out_new
    def __exit__(self, *args):
        sys.stdout = self.out_old

print ('A')
# withの入れ子を一行で書いている
with open('out.log', mode='w', encoding='utf-8') as a_file, RedirectStdoutTo(a_file):
    print ('書き込みました')
    
