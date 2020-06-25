def find_one(num):
    return num & (-num)

    # -num = ~num + 1


if __name__ == '__main__':
    print(find_one(10), bin(10))  # 2 -> 10(2)
