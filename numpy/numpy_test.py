#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import numpy

# numpyのバージョンを表示
print(numpy.version.version)

# Numpy内のdocstringからキーワードから必要になりそうな機能をリストアップ
# 時間かかるのでコメントアウト
# numpy.lookfor('array')

# ndarrayオブジェクトの生成にはarray()を使う
# arrayという型があるわけではないので注意
a = numpy.array([1,2,3,4,5])
print(a)
# 型はndarray
print(type(a))

b = numpy.array([[1,2,3,4,5],
                 [6,7,8,9,10]])
print(b)

# float型のarray
a = numpy.array([1,2,3], dtype=float)
print(a)
# 型を確認　ここでは'float64'
print(a.dtype)


# 0~5までの連続値を生成し、2x3行列を作る
# 数字の並びは [[0, 1, 2], [3, 4, 5]]
a = numpy.arange(6).reshape(2, 3)
print(a)

# 多次元arrayをリスト化する2つの方法
# ravelは「もつれをほぐす」という意味
b = numpy.ravel(a)
print(b)
b = a.flatten()
print(b)

# array にスカラーを足したり掛けたりすると、全要素に作用する
a = numpy.array([1,2,3])
print(a + 10)
print(a * 10)

# array同士の足し算 -> 要素ごとに和をとる
a = numpy.array([1,2,3])
b = numpy.array([5,6,7])
print(a+b)

# array同士の掛け算 -> 要素ごとに積をとる
a = numpy.array([1,2,3])
b = numpy.array([5,6,7])
print(a*b)

# 内積は.dot, 外積は.cross
a = numpy.array([1,2,3])
b = numpy.array([5,6,7])
print(numpy.dot(a,b))
print(numpy.cross(a,b))

# 各要素を2乗
a = numpy.array([1,2,3])
print(numpy.power(a, 2))


# [10, 20)からランダムに100個整数を生成
randoms = numpy.random.randint(10,20,100)
print(randoms)

# 全要素の和
print('sum =', randoms.sum())
# 算術平均
print('mean =', numpy.mean( randoms ))

# 中央値
print('median =', numpy.median( randoms ))
# 分散
print('var =', numpy.var( randoms ))
# 標準偏差
print('std =', numpy.std( randoms ))

# 自力で平均を求めると
avg = randoms.sum()/len(randoms)
print(avg)
# 自力で分散を求めると
var = numpy.mean( numpy.power( randoms - avg, 2 ) )
print(var)
# 自力で標準偏差を求めると
std = numpy.sqrt( var )
print(var)


# 最大値、最小値
print( numpy.amin(randoms) )
print( numpy.amax(randoms) )

# a{min,max}の代わりに{min, max}でもいけるようだ
# 
print( numpy.min(randoms) )
print( numpy.max(randoms) )
