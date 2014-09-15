#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""parse iTunes XML
Example:
   python itunes_xml_parse.py (itunes_xml_path)
"""

import os
import sys

import xml.etree.ElementTree as etree_dummy
from lxml import etree

def usage():
    print("usage: {0} (itunes_xml_path)".format(sys.argv[0]))


def dfs(root, depth):
    for child in root:
        print ("  " * depth, child.tag, ": ", child.text )
        dfs(child, depth + 1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        sys.exit(0)

    # XMLを読み込み
    xml_path = sys.argv[1]
    tree = etree.parse(xml_path)
    
    root = tree.getroot()

    # dfs(root, 1)

    songs = root.findall('./dict/dict/dict')

    # 曲ごとの情報を取得
    song_info_list = [] 
    for song in songs:
        song_info = {}
        key = ""
        for element in song:
            if element.tag == "key":
                key = element.text
            else:
                song_info[ key ] = element.text
        song_info_list.append( song_info )

        # for k,v in song_info.items():
        #     print(k, ": ", v)
        
        
    print(len(song_info_list))

    # 情報抽出
    artist_counter = {}
    for song_info in song_info_list:
        # たまに"Artist"の項目が空のことがある
        if "Artist" not in song_info:
            continue
        # podcastは除外
        elif "Genre" in song_info and song_info["Genre"] == "Podcast":
            continue

        artist_counter[ song_info["Artist"] ] = artist_counter.get( song_info["Artist"], 0 ) + 1

    # print( artist_counter )

    # ソート
    for i, k in enumerate(sorted(artist_counter, key=artist_counter.get, reverse=True)):
        if i >= 10: break
        # PodCastはスキップ
        print (k, artist_counter[k])
        
    

