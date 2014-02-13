#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

s = 'abcdefghi'
print(s.replace('ghi', 'ZZZ'))
print(re.sub('ghi$', 'ZZZ', s))

# 世紀表現
pattern = r'<a href="(.*?)">'
s = '<a href="a.html">aaa</a> <a href="b.html">bbb</b>'
match = re.findall(pattern, s)
print (match)

# 冗長な正規表現
# 半角スペースが使えなくなるので注意
pattern = '''
<a\s*href="
(.*?)  # url
">
'''
s = '<a href="a.html">aaa</a> <a href="b.html">bbb</b>'
match = re.findall(pattern, s, re.VERBOSE)
print (match)





