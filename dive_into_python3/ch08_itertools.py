#!/bin/env python3
# -*- coding: utf-8 -*-

import re, itertools

# e.g. "SEND + MORE = MONEY"
def solve(puzzle):
    words = re.findall('[A-Z]+', puzzle.upper())
    # すべての文字集合
    # e.g. {'E', 'D', 'M', 'O', 'N', 'S', 'R', 'Y'}
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    # 1文字目の文字集合
    
    first_letters = {word[0] for word in words}
    n = len(first_letters)

    # e.g. "SMEDONRY"
    sorted_characters = ''.join(first_letters) + \
                       ''.join(unique_characters - first_letters)
    

    # []ではなく()で囲うとジェネレータ式になる
    # 使い捨てる場合はリスト内包表記よりジェネレータ式のほうが効率がよい
    # e.g. (83, 77, 69, 68, 79, 78, 82, 89)
    characters = tuple(ord(c) for c in sorted_characters)

    # digits = (48, 49, 50, 51, 52, 53, 54, 55, 56, 57)
    digits = tuple(ord(c) for c in '0123456789')
    
    zero = digits[0]
    # digitsから取った8個の数字の全組み合わせを試す
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:
            # dict(zip(characters, guess)): 文字の置換方法を記述
            # .translate()によりその置換を実行
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation



                
if __name__ == '__main__':

    # nP2
    for i in itertools.permutations('ABC', 2):
        print (i)

    # 直積
    for i in itertools.product('ABC', [1,2,3]):
        print (i)

    # nC2
    for i in itertools.combinations('ABC', 2):
        print (i)

    import sys
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)



