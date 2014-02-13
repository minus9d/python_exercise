#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

str = '日本語の文字列です'
# python2なら27
# python3なら9
print (len(str))

# python3ならうまくいく
print (str[0])

# format
# {のエスケープは{{
# :.5fはフォーマット指定子
str = '{{1}} {0:.5f} {1} {2}'.format(100.3456789012, 'あああ', [1, 2, 3])
print(str)

# 合成フィールド
mylist = [10, 20, 30]
print( '{0[0]} {0[1]} {0[2]}'.format(mylist) )

# sys.moduleはdictionaryになってる
for (key, value) in sys.modules.items():
    print (key, value)

s = '''aaa
bbb
ccc
DdD
eee'''
print (s)

print(s.splitlines())
print(s.lower())
print(s.lower().count('d'))

query = 'a=b&c=d&e=f'
a_list = query.split('&')
print(a_list)
# splitは、一度だけ分割する
a_list_of_list = [elem.split('=', 1) for elem in a_list]
print(a_list_of_list)
# リストのリストから辞書作成
a_dict = dict(a_list_of_list)
print(a_dict)

# バイトリテラル
by = b'abcd\x65'
print (by)
print (type(by))
print (len(by))
for b in by:
    print (b)
print()
# error
# by[0] = 100 
barray = bytearray(by)
barray[0] = 100
print(barray)
print(type(barray))

# byte -> string
str = by.decode('ascii')
print(type(str))
print(str.count('d'))

# bytearray -> string
str = barray.decode('ascii')
print(type(str))
print(str.count('d'))

# string -> byte(utf-8)
string = 'これは日本語です'
by = string.encode('utf-8')
print(by)
# string -> byte(euc-jp)
by = string.encode('euc-jp')
print(by)
# string -> byte(sjis)
by = string.encode('sjis')
print(by)
# error
# by = string.encode('unknown_encoding')
# print(by)





       
