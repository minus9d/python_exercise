#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""parse iTunes XML
Example:
   python itunes_xml_parse.py (itunes_xml_path)
"""

import os
import sys
import collections
import pickle

import xml.etree.ElementTree as etree_dummy
from lxml import etree


def usage():
    print("usage: {0} (itunes_xml_path)".format(sys.argv[0]))


def read_song_info_list_from_xml( xml_path ):
    # XMLを読み込み
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
                # TODO: keyの種類によって, 文字列から適切な型に変換すべき
                song_info[ key ] = element.text
        song_info_list.append( song_info )

        # for k,v in song_info.items():
        #     print(k, ": ", v)

    return song_info_list
    

def dfs(root, depth):
    for child in root:
        print ("  " * depth, child.tag, ": ", child.text )
        dfs(child, depth + 1)

def artists_with_many_songs(song_info_list, top = 10):

    counter = collections.Counter()
    for song_info in song_info_list:
        # たまに"Artist"の項目が空のことがある
        if "Artist" not in song_info:
            continue
        # podcastは除外
        elif "Genre" in song_info and song_info["Genre"] == "Podcast":
            continue

        counter[ song_info["Artist"] ] += 1

    # 曲数の多いものの上位top個を返す
    return counter.most_common(10)
    
def most_played_songs(song_info_list, top = 10):
    top_ranked = sorted(song_info_list, key=lambda s: int(s.get("Play Count", "0")), reverse=True)[:top]
    return [ (i.get("Name", ""), i.get("Play Count", "0")) for i in top_ranked ]

# 共通部分のくくりだし
def most_played_items(song_info_list, tag, top = 10, per_song = False):
    item2play = collections.Counter()
    item2song = collections.Counter()
    for song_info in song_info_list:
        if tag in song_info and "Play Count" in song_info:
            item2play[ song_info[tag] ] += int(song_info["Play Count"])
            item2song[ song_info[tag] ] += 1

    if per_song:
        item2playpersong = {}
        for key in item2play:
            item2playpersong[ key ] = item2play[ key ] / item2song[ key ]
        top_ranked = sorted(item2playpersong, key=item2playpersong.get, reverse=True)[:top]
        
        return [ ( a, item2playpersong[a] ) for a in top_ranked ]
    else:
        return item2play.most_common(top)
    
def most_played_artists(song_info_list, top = 10, per_song = False):
    return most_played_items(song_info_list, "Artist", top, per_song)

def most_played_albums(song_info_list, top = 10, per_song = False):
    return most_played_items(song_info_list, "Album", top, per_song)

        
def release_year(song_info_list):
    release_year = collections.Counter()
    for song_info in song_info_list:
        if "Year" in song_info:
            y = int(song_info["Year"])
            release_year[y] = release_year.get(y, 0) + 1
    return release_year

def play_times_histogram(song_info_list):
    pass
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        usage()
        sys.exit(0)

    pickle_filename  = 'song_info_list.pickle'
    if os.path.exists(pickle_filename):
        with open(pickle_filename, 'rb') as f:
            song_info_list = pickle.load(f)
    else:
        xml_path = sys.argv[1]
        song_info_list = read_song_info_list_from_xml( xml_path )
        with open(pickle_filename, 'wb') as f:
            pickle.dump(song_info_list, f)
        

    print(len(song_info_list))
    

    print("\n[artists_with_many_songs]")
    print(artists_with_many_songs(song_info_list, 10))

    print("\n[most played songs]")
    print(most_played_songs(song_info_list, 10))

    print("\n[most played artists]")
    print(most_played_artists(song_info_list, 10))

    print("\n[most played artists (per song)]")
    print(most_played_artists(song_info_list, 10, per_song = True))

    print("\n[most played albums]")
    print(most_played_albums(song_info_list, 10))

    print("\n[most played albums (per song)]")
    print(most_played_albums(song_info_list, 10, per_song = True))

    print("\n[release year]")
    print(release_year(song_info_list))

    
        
    

