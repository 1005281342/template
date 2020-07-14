from typing import List
from collections import defaultdict


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


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        """
        先判断有没有入度为 2 的点：
        没有入度为 2 的点：则一定有首尾相接的圈（意思是箭头方向全是一致，全是顺时针或者逆时针），
        此时可以按照无向图的情形处理，删除最后出现的多余的边。
        有入度为 2 的点 c，两条边先后出现的顺序是 [a,c] 和 [b,c]：在边集中去掉 [b,c]，
        判断剩下的边集中是否存在圈： a. 如果存在圈，则删掉 [a,c]。 b. 不存在圈，则删掉 [b,c].
        """
        dd = defaultdict(list)

        flag = False
        # 找到入度为2的点
        for a, b in edges:
            dd[b].append(a)
            if len(dd[b]) == 2:
                flag = True
                break

        # 选择其中一组移除假如选择（list(dd[b])[1], b）添加
        if flag:
            dsu = DSU(1010)
            for a, c in edges:
                # 不添加（list(dd[b])[1], b）
                if a == dd[b][1] and c == b:
                    continue
                dsu.union(a, c)

            if not dsu.union(dd[b][1], b):
                return [dd[b][1], b]
            else:
                return [dd[b][0], b]

        # 没有出现入度为2的点，则可以当作无向图处理
        dsu = DSU(1010)
        for a, c in edges:
            if not dsu.union(a, c):
                return [a, c]
        return list()
