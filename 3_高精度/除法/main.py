# 高精度整数除以整数
def div(a: str, b: int):
    t = 0
    ans_list = list()
    for c in a:
        ans_list.append(str((t * 10 + int(c)) // b))
        t = (t * 10 + int(c)) % b

    ans = str()
    index = 0
    while index < len(ans_list):
        if ans_list[index] == '0':
            index += 1
            continue
        else:
            ans = ans_list[index]
            index += 1
            break

    while index < len(ans_list):
        ans += ans_list[index]
        index += 1
    return ans


if __name__ == '__main__':
    from random import randint

    for _ in range(1024):
        a = randint(100000, 1000000)
        b = randint(100, 10000)
        if div(str(a), b) != str(a // b):
            print(a, b, div(str(a), b), a // b)
