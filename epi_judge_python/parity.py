from test_framework import generic_test


def parity_bruteforce(x: int) -> int:
    p = 0
    while x:
        p ^= x & 1
        x >>= 1
    return p


def parity_bruteforce_refined(x: int) -> int:
    p = 0
    while x:
        p ^= 1
        x = x & x - 1
    return p


def parity(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


def test(s: str) -> None:
    print(f'{s}')
    generic_test.generic_test_main('parity.py', 'parity.tsv', eval(s))
    print('----------------------------------------')


if __name__ == '__main__':
    test('parity_bruteforce')
    test('parity_bruteforce_refined')
    test('parity')
