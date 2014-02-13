#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)     

def rules(rules_filename):
    # withによりコンテクストを作り、自動でファイルを閉じることができる
    with open(rules_filename, encoding='utf-8') as pattern_file:
        for line in pattern_file:
            # 空白文字で分割
            # 末尾の改行は含まれないらしい
            pattern, search, replace = line.split(None, 3)
            yield build_match_and_apply_functions(pattern, search, replace)

def plural(noun, rules_filename = 'ch06_rules.txt'):
    for matches_rule, apply_rule in rules(rules_filename):
        if matches_rule(noun):
            return apply_rule(noun)
    raise ValueError('no matching rule for {0}'.format(noun))

# 1
print (plural('index'))
# 2
print (plural('dish'))
# 3
print (plural('fly'))
# 4
print (plural('boy'))
print (plural('dot'))


# ジェネレータを使った関数
def make_counter(x):
    print('entering make_counter')
    while True:
        yield x
        print('incrementing x')
        x = x + 1

counter = make_counter(2)
print(next(counter))
print(next(counter))
print(next(counter))


# ジェネレータの別の例
def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b
fibo = fibonacci(1000)
for n in fibonacci(1000):
    print(n, end = ' ')
print()
print(list(fibonacci(1000)))

