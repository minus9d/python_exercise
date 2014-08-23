#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class MyClass:
    """はじめてのクラス"""
    val = 777

    # コンストラクタ
    def __init__(self, val):
        self.val = val

    # デストラクタ
    def __del__(self):
        print('destructor is called.')
        pass
    
    def print(self):
        print(self.val)
    def print2(self, msg):
        print(self.val, " + ", msg)

    def __private_func(self):
        print("can't called from outside")

    __private_val = 100


class Base:
    def func(self):
        print("Base.func()")

class Derived(Base):
    # オーバーライド
    def func(self):
        super().func()
        print("Derive.func()");

class ClassWithSpecialMethods():
    val = 300
    # オブジェクトの情報を表す文字列を返す
    # 曖昧性をなくすための文字列を返す
    def __repr__(self):
        return "val = " + str(self.val)
    # 実装しない場合は__repr__が呼ばれる
    # 人が見て理解しやすい文字列を返す
    # __repr__との違いは http://stackoverflow.com/questions/1436703/difference-between-str-and-repr-in-python に詳しい
    def __str__(self):
        return "val = " + str(self.val)

    # よくわからない
    def __bytes__(self):
        pass
    
    def __bool__(self):
        return bool(self.val)
        
def cannot_release_instance_because_of_destructor():
    obj1 = MyClass(10)
    obj2 = MyClass(10)
    obj1.other = obj2
    obj2.other = obj1
    del obj1, obj2

    # ガベージコレクションを実行
    import gc
    gc.collect()
    # まだobj1, obj2が解放されていないことがわかる
    print(gc.garbage)


def inheritance():
    d = Derived()
    d.func()

def special_method():
    c = ClassWithSpecialMethods()
    print("repr = ", str(repr(c)))
    print("str = ", str(c))

    # よくわからない
    # b = bytes(c)

    print("format = ", format(c))
    print("hash = ", hash(c))
    print("bool = ", bool(c))

def private_member():
    obj = MyClass(-99)

    try:
        obj.__private_func()
    except:
        print ("error has occured.")

    try:
        print ("private val = ", obj.__private_val)
    except:
        print ("error has occured.")
    
obj = MyClass(-99)

# 勝手に属性を設定できる
obj.x = 100
obj.y = 200
del obj.x
del obj.y
obj.print()
obj.print2("message")

# 循環参照を作ってしまったせいでインスタンスが解放されない例
cannot_release_instance_because_of_destructor()

# 継承テスト
inheritance()

# 特殊メソッドのテスト
special_method()

# __で始まるメンバにはアクセスできない
private_member()
