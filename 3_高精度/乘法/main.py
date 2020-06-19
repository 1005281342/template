from random import randint


# 高精度整数乘整数
def mul(a: str, b: int):
    a_list = [int(c) for c in reversed(list(a))]

    ans_list = list()
    t = 0
    for c in a_list:
        x = ((c * b) + t) % 10
        ans_list.append(str(x))
        t = ((c * b) + t) // 10
    # print(ans_list)
    ans = str()

    if not t:
        while ans_list:
            ta = ans_list.pop()
            if ta == '0':
                continue
            else:
                ans = ta
                break
    else:
        ans = str(t)

    while ans_list:
        ans += ans_list.pop()

    # print(ans)
    return ans


if __name__ == '__main__':

    for _ in range(1024):
        a = randint(100000, 1000000)
        b = randint(100, 10000)
        if mul(str(a), b) != str(a * b):
            print(a, b)
