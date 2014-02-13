#!/usr/bin/env python3
# -*- coding: utf-8 -*-


a = ['a', 3, 'd']
a.append('added')
print (a)
print (a[0])
print (a[-1])
# error
# print (a[-10])

# OK
a.insert(20, 'sss')
print (a)

a.extend([10, True, 2.2])
print (a)

# Probably this is not what you want
a.append([10, True, 2.2])
print (a)


print (a.count(2.2))
print (a.count(2.9))
print (True in a)
print (False in a)

print (a.index(2.2))

# error
# print (a.index(2.9))

print (a)
del a[1]
print (a)

b = [3, 3, 3, 3, 3]
# first 3 is removed
b.remove(3)
print (b)


print (a)
popped = a.pop(4)
print(popped)
print (a)


c = ("a", "b")
print(c)
# error
# c[0] = "d"

# make a tuple from a list
d = tuple(a)
print (d)

# make a list from a tuple
e = list(d)
print (e)

# tuple with only one member
f = (1,)

# 0, 1, 2
(MON, TUE, WED) = range(3)
print (MON)


# set
g = {2, 3, 5, 7}
h = {2, 4, 6, 8}
print (g)

# this is not a set but a dictionary
i = {}
print (type(i))

# this is a set
i = set()
print (type(i))

g.update({10, 20})
g.add(77)
print (g)

# safe
g.discard(77)
g.discard(77)
g.discard(77)
print (g)

g.remove(2)
# error
# g.remove(2)
print (g)



# ややこしい型

def show_type(a):
    print( type(a) )
    

# 整数型
show_type( 3 )
show_type( (3) )

# リスト
show_type( [] )
show_type( [1, 2, 3] )

# タプル
show_type( () )
show_type( (3,) )
show_type( (3, 4) )

# 辞書
show_type( {} )
show_type( {"key1": 1, "key2": 2} )

# 集合
show_type( set() )
show_type( {2, 3, 5} )
