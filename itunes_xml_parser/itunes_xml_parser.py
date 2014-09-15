#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""parse iTunes XML
Example:
   python itunes_xml_parse.py (itunes_xml_path)
"""


import os
import sys
import pickle
import xml.etree.ElementTree as etree 

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


    tree = None
    pickle_filename  = 'xml.pickle'

    if os.path.exists(pickle_filename):
        with open(pickle_filename, 'rb') as f:
            tree = pickle.load(f)  
        
    else:
        xml_path = sys.argv[1]
        print(xml_path)
        tree = etree.parse(xml_path)
        
        with open(pickle_filename, 'wb') as f:
            pickle.dump(tree, f)
    
    root = tree.getroot()
    print(tree)

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
            

    #dfs(root, 1)

    # いい感じ
    songs = root.findall('./dict/dict/dict')

    
    
    print(songs)
    
    

