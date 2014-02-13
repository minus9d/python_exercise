#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __iter__()メソッドを持つクラスはイテレータとなる
class Fib:
    ''' iterator that yields numbers in the Fibonacci sequence'''

    # 最初に呼ばれる
    def __init__(self, max):
        self.max = max

    # 誰かがiter(fib)を呼び出した時に呼び出される
    # 呼び出されたら、__nex__()メソッドを実装した何らかのオブジェクトを返す
    # （ここではクラス自身）
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self
    # 誰かがイテレータクラスのインスタンスについてnext()を呼び出すと、このメソッドが呼び出される
    def __next__(self):
        fib = self.a
        if fib > self.max:
            # イテレータの終了を意味する例外を投げる。この例外はエラーではない
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib
        

# passは何も行わない    
class Empty:
    pass


fib = Fib(100)
print(fib)
print(fib.__class__)
# docstringを表示
print(fib.__doc__)


for n in fib:
    print (n, end = ' ')
print ()



import ch06_generators
class LazyRules:
    # クラス変数（すべてのインスタンスによって共有される）
    # インスタンス変数と違い、"self."が付かない
    rules_filename = 'ch06_rules.txt'

    def __init__(self):
        self.pattern_file = open(self.rules_filename, encoding='utf-8')
        self.cache = []

    # 誰かがiter(rules)を呼び出すたびに呼び出される
    # イテレータ（ここでは自分自身）を返す
    def __iter__(self):
        self.cache_index = 0
        return self

    # 誰か（例えばforループ）がnext(rules)を呼び出すたびに呼び出される
    def __next__(self):
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]
        if self.pattern_file.closed:
            raise StopIteration
        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration
            
        pattern, search, replace = line.split(None, 3)
        funcs = ch06_generators.build_match_and_apply_functions(pattern, search, replace)
        self.cache.append(funcs)
        return funcs

rules = LazyRules()

# 1
print (ch06_generators.plural('index'))
# 2
print (ch06_generators.plural('dish'))
# 3
print (ch06_generators.plural('fly'))
# 4
print (ch06_generators.plural('boy'))
print (ch06_generators.plural('dot'))



# クラス変数の実験
r1 = LazyRules()
r2 = LazyRules()
print (r1.rules_filename)
print (r2.rules_filename)
print (r1.__class__.rules_filename)
print (r2.__class__.rules_filename)
# インスタンスの属性値を変えても、他のインスタンスの属性値には影響を与えない
r1.rules_filename = 'override.txt'
print (r1.rules_filename)
print (r2.rules_filename)
print (r1.__class__.rules_filename)
print (r2.__class__.rules_filename)
# クラス属性を変更すると、値を受け継いでいるインスタンスはその影響を受ける
r2.__class__.rules_filename = 'override-2.txt'
print (r1.rules_filename)
print (r2.rules_filename)
print (r1.__class__.rules_filename)
print (r2.__class__.rules_filename)


