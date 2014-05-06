#!/usr/bin/env python3
# -*- coding: utf-8 -*-

global_val = 'aaa';

def func():
    # グローバル変数を使用することを宣言
    global global_val
    global_val = 'bbb';


if __name__ == '__main__':
    print (global_val)
    func()
    print (global_val)
    
