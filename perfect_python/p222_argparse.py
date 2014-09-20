#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()

# 値を必要とする引数
# default以下に、引数が指定されなかったときの値を書く
parser.add_argument('-f', '--file', default="default_file.txt", help="set input file path")

# 値を必要としない引数
# actionに'store_true'を指定すると、値を必要としないという意味になる
parser.add_argument('-v', '--verbose', action='store_true', help="verbose output")

# 結果を出力
args = parser.parse_args()
print(args)
print(args.file)
print(args.verbose)
