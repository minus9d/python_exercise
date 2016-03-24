#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# csvファイルの読み込み
# 参考:
#   http://softwarerecs.stackexchange.com/questions/7463/fastest-python-library-to-read-a-csv-file
#   http://qiita.com/okadate/items/c36f4eb9506b358fb608
#   http://stackoverflow.com/questions/29451030/why-doesnt-np-genfromtxt-remove-header-while-importing-in-python
#   http://stackoverflow.com/questions/19302859/getting-header-row-from-numpy-genfromtxt
#   http://www.mwsoft.jp/programming/numpy/csv.html

import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas

csvfile = 'data.csv'
delimiter = ','

def open_with_python_csv(filename):
    data = []
    with open(filename, 'r') as filename:
        reader = csv.reader(filename, delimiter=delimiter)

        # ヘッダ行は特別扱い
        header = next(reader)

        # 中身
        for row in reader:
            #data.append(row)
            data.append([float(x) for x in next(reader)])

    return header, data

def open_with_pandas(filename):
    df = pandas.read_csv(filename)

    header = df.columns.values.tolist()
    data = df.values

    return df, header, data

def open_with_numpy_loadtxt(filename):
    # ヘッダ行は読み飛ばして捨ててしまう場合の書き方
    # 以下の必要あり
    #   ・デリミタの指定
    #   ・読み飛ばす行数の指定
    data = np.loadtxt(filename, delimiter=',', skiprows=1)
    return data

def open_with_numpy_loadtxt_2(filename):
    # ヘッダ行も得る場合の書き方　その1
    with open(filename, 'r') as file:
        # 1行だけ読んで、ヘッダ行を取得
        line = file.readline()
        header = line.strip().split(',')
        # 残りをloadtxtで読む
        data = np.loadtxt(file, delimiter=',')
    return header, data

def open_with_numpy_loadtxt_3(filename):
    # ヘッダ行も得る場合の書き方　その2
    # 全行一気に読み込む
    with open(filename, 'r') as file:
        lines = list(file)
    # 最初の行はヘッダ行
    header = lines[0].strip().split(',')
    # 2行目以降はデータ行
    data = np.loadtxt(lines[1:], delimiter=',')
    return header, data

def open_with_numpy_genfromtxt(filename):
    # ヘッダ行は読み飛ばして捨ててしまう場合の書き方
    # 以下の必要あり
    #   ・デリミタの指定
    #   ・読み飛ばす行数の指定
    data = np.genfromtxt(filename, delimiter=',', skip_header=1)
    return data

def open_with_numpy_genfromtxt_2(filename):
    # names=Trueとすると、ヘッダの情報がdtype.namesに入る
    data = np.genfromtxt(filename, delimiter=',', names=True)
    header = data.dtype.names
    return header, data

def main():
    header, data = open_with_python_csv(csvfile)
    print("header:", header)
    print("data:", data)
    print("type(data):", type(data))
    print()

    df, header, data = open_with_pandas(csvfile)
    print("df:", df) # pandasの操作を行うときはdfを使う
    print("header:", header)
    print("data:", data)
    print("type(df):", type(df))
    print("type(header):", type(header))
    print("type(data):", type(data))
    print()

    data = open_with_numpy_loadtxt(csvfile)
    print("data:", data)
    print("type(data):", type(data))
    print()

    header, data = open_with_numpy_loadtxt_2(csvfile)
    print("header:", header)
    print("data:", data)
    print("type(data):", type(data))
    print()

    header, data = open_with_numpy_loadtxt_3(csvfile)
    print("header:", header)
    print("data:", data)
    print("type(data):", type(data))
    print()

    data = open_with_numpy_genfromtxt(csvfile)
    print("data:", data)
    print("type(data):", type(data))
    print()

    header, data = open_with_numpy_genfromtxt_2(csvfile)
    print("header:", header)
    print("data:", data)
    print()


main()
