#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# matplotlibをオブジェクト指向らしく使う
# 参考: http://matplotlib.org/examples/pylab_examples/pythonic_matplotlib.html

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 1.0, 0.01)

####################
#1つ目のウィンドウ
####################
fig1 = plt.figure(1)

# axはaxesのこと。線やテキストを加える矩形領域に相当。
# figureの中に1個以上のaxが存在する。
ax1 = fig1.add_subplot(211)
ax1.plot(t, np.sin(2*np.pi*t))
ax1.grid(True)
ax1.set_ylim( (-2,2) )
ax1.set_ylabel('1 Hz')
ax1.set_title('A sine wave or two')

for label in ax1.get_xticklabels():
    label.set_color('r')

ax2 = fig1.add_subplot(212)
ax2.plot(t, np.sin(2*2*np.pi*t))
ax2.grid(True)
ax2.set_ylim( (-2,2) )
l = ax2.set_xlabel('Hi mom')
l.set_color('g')
l.set_fontsize('large')


####################
#2つ目のウィンドウ
####################
fig2 = plt.figure(2)

# axはaxesのこと。線やテキストを加える矩形領域に相当。
# figureの中に1個以上のaxが存在する。
ax1 = fig2.add_subplot(211)
ax1.plot(t, np.cos(2*np.pi*t))
ax1.grid(True)
ax1.set_ylim( (-2,2) )
ax1.set_ylabel('1 Hz')
ax1.set_title('A sine wave or two')

for label in ax1.get_xticklabels():
    label.set_color('r')

ax2 = fig2.add_subplot(212)
ax2.plot(t, np.cos(2*2*np.pi*t))
ax2.grid(True)
ax2.set_ylim( (-2,2) )
l = ax2.set_xlabel('Hi mom')
l.set_color('g')
l.set_fontsize('large')


plt.show()
