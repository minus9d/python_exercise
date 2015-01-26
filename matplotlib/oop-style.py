#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# matplotlibをオブジェクト指向らしく使うサンプル
# 2つのグラフ(axes)を含む図(figure)を、2つ作成。表示して保存
# 参考:
#   http://bicycle1885.hatenablog.com/entry/2014/02/14/023734
#   http://matplotlib.org/examples/pylab_examples/pythonic_matplotlib.html

import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

def main():

    t = np.arange(0.0, 1.0, 0.01)
    
    ####################
    #1つ目のウィンドウ
    ####################
    fig1 = plt.figure(1)
    
    ################################
    #1つ目のウィンドウ 1つ目のグラフ
    ################################
    ax1 = fig1.add_subplot(211)
    ax1.plot(t, np.sin(2*np.pi*t))
    ax1.grid(True)
    ax1.set_ylim( (-2,2) )
    ax1.set_xlabel('t')
    ax1.set_ylabel('f(t)')
    ax1.set_title('sin function')
    
    ################################
    #1つ目のウィンドウ 2つ目のグラフ
    ################################
    ax2 = fig1.add_subplot(212)
    ax2.plot(t, np.cos(2*np.pi*t))
    ax2.grid(True)
    ax2.set_ylim( (-2,2) )
    ax2.set_xlabel('t')
    ax2.set_ylabel('f(t)')
    ax2.set_title('cos function')
    


    ####################
    # 2つ目のウィンドウ
    ####################
    fig2 = plt.figure(2)

    ################################
    # 2つ目のウィンドウ 1つ目のグラフ
    ################################
    # 等高線
    ax1 = fig2.add_subplot(211)
    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X,Y = np.meshgrid(x, y)

    ax1.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
    C = ax1.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
    ax1.clabel(C, inline=1, fontsize=10)
    ax1.set_title('contour')

    ################################
    # 2つ目のウィンドウ 2つ目のグラフ
    ################################
    ax2 = fig2.add_subplot(212)
    ax2.plot([1, 4, 3, 6, 5, 9])
    ax2.grid(True)
    ax2.set_ylabel('values')
    ax2.set_title('points')
    


    ################################
    # 2つのウィンドウを表示
    ################################
    fig1.tight_layout()  # グラフの文字がかぶらないようにする
    fig2.tight_layout()  # グラフの文字がかぶらないようにする
    plt.show()
    
    ################################
    # 2つの画像を保存
    ################################
    fig1.savefig('fig1.png')
    fig2.savefig('fig2.png')


main()
