#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 「入力の数字がnの倍数のときのみTrueを返す関数」を返す関数
def is_multiple_of_n(n):
    return lambda x: x % n == 0

def is_multiple_of_3(n):
    return n % 3 == 0


nums = range(30)
filtered_nums = filter(is_multiple_of_3, nums)

print(list(filtered_nums))


nums = range(30)

# 7の倍数のみ抽出
filtered_nums = filter(is_multiple_of_n(7), nums)
print(list(filtered_nums))

# 5の倍数のみ抽出
filtered_nums = filter(is_multiple_of_n(5), nums)
print(list(filtered_nums))



    
