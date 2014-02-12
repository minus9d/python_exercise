#!/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as etree
tree = etree.parse('ch12_feed.xml')
root = tree.getroot()

# <Element '{http://www.w3.org/2005/Atom}feed' at 0xffdcd16c>
print(root)

# {http://www.w3.org/2005/Atom}feed
print(root.tag)

# 子要素の数 = 8
print(len(root))

# 子要素を順番に取得
# <Element '{http://www.w3.org/2005/Atom}title' at 0xffdcd26c>
# <Element '{http://www.w3.org/2005/Atom}subtitle' at 0xffdcd36c>
# <Element '{http://www.w3.org/2005/Atom}id' at 0xffdcd40c>
# <Element '{http://www.w3.org/2005/Atom}updated' at 0xffdcd4ac>
# <Element '{http://www.w3.org/2005/Atom}link' at 0xffdcd60c>
# <Element '{http://www.w3.org/2005/Atom}entry' at 0xffdcd68c>
# <Element '{http://www.w3.org/2005/Atom}entry' at 0xffdcde2c>
# <Element '{http://www.w3.org/2005/Atom}entry' at 0xffdd130c>
for child in root:
    print(child)

# {'{http://www.w3.org/XML/1998/namespace}lang': 'en'}
print(root.attrib)

# 5番目の子を表示
# <Element '{http://www.w3.org/2005/Atom}link' at 0xffdcd60c>
print (root[4])

# {'href': 'http://diveintomark.org/', 'type': 'text/html', 'rel': 'alternate'}
print (root[4].attrib)

# クエリにマッチする子要素をすべて見つける
# ここでは、ルート要素が持つentryという名前の子が検索される
print(root.findall('{http://www.w3.org/2005/Atom}entry'))

# rootの代わりにtreeと書いても同じ
print(tree.findall('{http://www.w3.org/2005/Atom}entry'))

# 子孫すべてから検索するためには//を付ける
all_links = tree.findall('//{http://www.w3.org/2005/Atom}link')
for link in all_links:
    print(link.attrib)

# XPath(クエリ言語)を使うには、lxmlライブラリを使う
# lxmlのほうが、組み込みのElementTreeより高速
# from lxml import etree
# 以下省略


# XML生成
import xml.etree.ElementTree as etree
new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed',
                         attrib={'{http://www.w3.org/XML/1998/namespace}lang': 'en'})
print('-----')
print(etree.tostring(new_feed))


