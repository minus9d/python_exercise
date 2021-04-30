"""
unittestの最小サンプル。

- python main.pyとするとunittestの結果が表示される
- python main.py -vとするとより冗長な結果が表示される
- python -m unittest main.MyTestClass.test_add1とすると特定のテストだけを選択的に実行

"""
import unittest


def add(x, y):
    return x + y


# テストケースは、`unittest.TestCase`クラスを継承することで作成
class AddTest(unittest.TestCase):

    # メソッド名が`test`で始まるメソッドの1個1個がテスト
    # メソッド名が`test`で始まらないと実行されないので注意
    def test_add(self):
        self.assertEqual(add(1, 2), 3)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
