#!/bin/env python3
# -*- coding: utf-8 -*-

import re

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)     

rules = []
# withによりコンテクストを作り、自動でファイルを閉じることが出来る
with open('ch06_rules.txt', encoding='utf-8') as pattern_file:
    for line in pattern_file:
        print ("[", line, "]")
        # 空白文字で分割
        # 末尾の改行は含まれないらしい
        pattern, search, replace = line.split(None, 3)
        print ("replace = ", replace, "]")
        rules.append(build_match_and_apply_functions(pattern, search, replace))

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)
# 1
print (plural('index'))
# 2
print (plural('dish'))
# 3
print (plural('fly'))
# 4
print (plural('boy'))
print (plural('dot'))

