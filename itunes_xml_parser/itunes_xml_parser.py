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
    print(tree)

    sys.exit()

    # root = "dict"
    # print(root)
    # print(root.tag)
    # print(root.attrib)
    print("root len = ", len(root))
    for child in root:
        print(child)
        print(child.tag)
        print(child.attrib)
        print(child.text)
        for c2 in child:
            print(c2)
            print(c2.tag)
            print(c2.attrib)
            print(c2.text)
            

    dfs(root, 1)

    # いい感じ
    songs = root.findall('./dict/dict/dict')

    
    
    print(songs)
    
    

