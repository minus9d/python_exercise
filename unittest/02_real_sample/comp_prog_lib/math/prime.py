"""
素数に関する関数を提供
"""


def is_prime(n: int):
    """nが素数か否かを判定"""
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
