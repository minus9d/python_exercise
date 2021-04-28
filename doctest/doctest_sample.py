#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# python -m doctest doctest_sample.py とすると、簡易的なユニットテストになる
# 以下ではわざと一つ間違えている
def add_to_n(n):
    """ 1からnまでの和を返す
    >>> add_to_n(0)
    0
    >>> add_to_n(1)
    1
    >>> add_to_n(10)
    54
    """
    return n * (n+1) // 2


def main():
    print(add_to_n(10))

if __name__ == '__main__':
    main()
