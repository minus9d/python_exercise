#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def counter():
    count = 0
    def _counter():
        # ローカルスコープではない一番近くの変数を利用
        nonlocal count
        count += 1
        return count
    return _counter

c = counter()
print(c())

