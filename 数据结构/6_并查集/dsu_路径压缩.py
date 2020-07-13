class DSU(object):

    def __init__(self, n):
        # n代表点的个数
        self.pre = [0] * n
        for i in range(n):
            self.pre[i] = i

    # 查找x的根节点，并进行路径压缩（注意使用路径压缩的话，独立集合的根结点不能初始化为一个相同值，比如-1）
    # 如 self.pre = [-1] * n，这样在合并时求解是否存在环的时候所找根节点都会为-1而造成误判
    def find(self, x: int):
        if self.pre[x] != x:
            self.pre[x] = self.find(self.pre[x])
        return self.pre[x]

    # 合并两个集合
    # False: 说明已经在一个集合中，无需合并
    # True: 合并成功
    def union(self, a: int, b: int) -> bool:
        ar = self.find(a)
        br = self.find(b)
        if ar == br:
            return False

        # 将a所在集合插入到b所在集合中
        self.pre[ar] = br
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
