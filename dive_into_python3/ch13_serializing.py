#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import pickle
import pickletools
import json

print(sys.getrecursionlimit())

entry = {}
entry['title'] = 'Dive into history, 2009 edition'
entry['article_link'] = 'http://diveintomark.org/archives/2009/03/27/dive-into-history-2009-edition'
entry['comments_link'] = None
entry['internal_id'] = b'\xDE\xD5\xB4\xF8'
entry['tags'] = ('diveintopython', 'docbook', 'html')
entry['published'] = True
import time
entry['published_date'] = time.strptime('Fri Mar 27 22:20:42 2009')   

# 書き込み
with open('entry.pickle', 'wb') as f:
    # シリアライズ
    pickle.dump(entry, f)

# 読み込み
with open('entry.pickle', 'rb') as f:
    entry_loaded = pickle.load(f)

print(entry_loaded)

# メモリ上にシリアライズ
# sはstreamのsと思われる
b = pickle.dumps(entry)
entry_loaded_from_memory = pickle.loads(b)
print(entry_loaded_from_memory)


# pickeプロトコルのバージョンを推測
# 何やってるのかよくわからん
def protocol_version(file_object):
    maxproto = -1
    for opcode, arg, pos in pickletools.genops(file_object):
        maxproto = max(maxproto, opcode.proto)
    return maxproto




# ファイルの逆アセンブル
with open('entry.pickle', 'rb') as f:
    pickletools.dis(f)


# バージョンを表示
with open('entry.pickle', 'rb') as f:
    print('version = ', protocol_version(f))


# JSON形式で保存
# タプルとバイト列はマッピングできない
# タプルをマッピングすると、勝手にJSONの配列に変えられてしまう
# バイト列をマッピングすると、エラーになる
basic_entry = {}
basic_entry['id'] = 256
basic_entry['title'] = 'Dive into history, 2009 edition'
basic_entry['tags'] = ('diveintopython', 'docbook', 'html')
basic_entry['published'] = True
basic_entry['comments_link'] = None
with open('basic.json', mode='w', encoding='utf-8') as f:
    #indentオプションにより読みやすくなる
    json.dump(basic_entry, f, indent=4)

print(type(entry["published_date"]))
    

# バイト列を保存するために、独自の「小さなシリアライズ形式」を定義する    
def to_json(python_object):
    # Dive Into Pythonではこれを書かないと例外が出ることになっていたが、
    # 特になくても例外出ない様子
    # そもそも、このifがtrueにならない？
    if isinstance(python_object, time.struct_time):
        return {'__class__': 'time.asctime',
                # 文字列化
                '__value__': time.asctime(python_object)}
    if isinstance(python_object, bytes):
        return {'__class__': 'bytes',
                # バイト列を整数のリストに変換
                '__value__': list(python_object)}

    raise TypeError(repr(python_object) + ' is not JSON serializable') 

print(entry)

# バイト列を含んだデータを、自作のエンコーダでJSONに保存
with open('entry.json', 'w', encoding='utf-8') as f:
    json.dump(entry, f, default=to_json, indent=4)


def from_json(json_object):
    if '__class__' in json_object:
        if json_object['__class__'] == 'time.asctime':
            return time.strptime(json_object['__value__'])
        if json_object['__class__'] == 'bytes':
            return bytes(json_object['__value__'])
    return json_object


# JSONを読み出し
with open('entry.json', 'r', encoding='utf-8') as f:
    read_entry = json.load(f)

print(read_entry)
