# a >= b; a>=0. b>=0
def sub(a, b):
    a_list = [int(c) for c in reversed(list(a))]
    b_list = [int(c) for c in reversed(list(b))]

    ans_list = list()
    t = 0
    for i in range(len(a)):
        t = a_list[i] - t
        if i < len(b):
            t -= b_list[i]
        ans_list.append((t + 10) % 10)
        if t < 0:
            t = 1
        else:
            t = 0

    ans = str()
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
        a = randint(10000, 1000000)
        b = randint(100, 10000)
        if sub(str(a), str(b)) != str(a - b):
            print(a, b)
