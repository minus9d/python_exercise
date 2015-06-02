#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python -m unittest discover
# とすると、このディレクトリ以下にあるユニットテストを探してすべて実行

import unittest


class Test(unittest.TestCase):

    def test_it(self):
        import doctest_sample
        self.assertEqual(15, doctest_sample.add_to_n(5))
        self.assertEqual(56, doctest_sample.add_to_n(10))
        self.assertEqual(5050, doctest_sample.add_to_n(100))
