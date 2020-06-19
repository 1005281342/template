def add(a: str, b: str):
    if len(a) < len(b):
        return add(b, a)

    # 从个位开始累加
    a_list = [int(c) for c in reversed(list(a))]
    b_list = [int(c) for c in reversed(list(b))]

    ans_list = list()
    t = 0
    for i in range(len(a)):
        t += a_list[i]
        if i < len(b):
            t += b_list[i]
        ans_list.append(t % 10)
        t //= 10

    ans = ""
    if not t:
        while ans_list:
            ta = str(ans_list.pop())
            if ta == '0':
                continue
            else:
                ans = ta
                break
    else:
        ans = str(t)

    while ans_list:
        ans += str(ans_list.pop())

    return ans


if __name__ == '__main__':
    from random import randint

    for _ in range(1024):
        a = randint(100000, 1000000)
        b = randint(100, 10000)
        if add(str(a), str(b)) != str(a + b):
            print(a, b, add(str(a), str(b)), a + b)
