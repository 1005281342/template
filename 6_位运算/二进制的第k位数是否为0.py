def is_zero(num, k):
    return not ((num >> k) & 1)


if __name__ == '__main__':
    print(is_zero(10, 2), bin(10))