class DSU(object):

    def __init__(self, n):
        # n代表点的个数
        self.pre = [0] * n
        for i in range(n):
            self.pre[i] = i

        # rank表示每个集合的高度
        self.rank = [0] * n

    # 查找x的根节点
    def find(self, x: int):
        while self.pre[x] != x:
            x = self.pre[x]
        return x

    # 合并两个集合
    # False: 说明已经在一个集合中，无需合并
    # True: 合并成功
    def union(self, a: int, b: int) -> bool:
        ar = self.find(a)
        br = self.find(b)
        if ar == br:
            return False

        if self.rank[ar] > self.rank[br]:
            self.pre[br] = ar
        elif self.rank[ar] < self.rank[br]:
            self.pre[ar] = br
        else:
            self.pre[ar] = br
            self.rank[br] += 1
        return True


if __name__ == '__main__':
    # 存在环CASE
    # edges = [
    #     (0, 1), (1, 2), (1, 3),
    #     (2, 4), (3, 4), (2, 5)
    # ]
    # 不存在环CASE
    edges = [
        (0, 1), (1, 2), (1, 3),
        (3, 4), (2, 5)
    ]
    n = 6
    dsu = DSU(n)
    for a, b in edges:
        if not dsu.union(a, b):
            raise print("存在环")

    print("不存在环")
