# https://leetcode-cn.com/problems/n-queens/
from typing import List


class Solution:

    def __init__(self):
        self.n = 0
        self.x = list()  # 竖行
        self.y = list()  # 横行
        self.dg = list()  # 左对角线: y = - x + b -> b = x + y
        self.udg = list()  # 右对角线: y = x + b -> b = y - x
        self.ans = list()
        self.path = list()

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.x = [False] * n * 2
        self.y = [False] * n * 2
        self.dg = [False] * n * 2
        self.udg = [False] * n * 2
        self.path = [['.'] * n for _ in range(self.n)]

        self.dfs(0, 0, 0)  # 从（0，0）点开始搜索，皇后放置个数为0
        return self.ans

    def dfs(self, x, y, cnt):
        # 当前行已经走完，需要换行
        if y == self.n:
            y = 0
            x += 1

        # 已经遍历完
        if x == self.n:
            # 找到一种可行方案
            if cnt == self.n:
                self.ans.append(["".join(x) for x in self.path])
            return

        self.dfs(x, y + 1, cnt)

        if self.x[x] or self.y[y] or self.dg[y + x] or self.udg[self.n + y - x]:
            return

        self.path[x][y] = "Q"
        self.x[x] = self.y[y] = self.dg[y + x] = self.udg[self.n + y - x] = True
        self.dfs(x, y + 1, cnt + 1)
        self.x[x] = self.y[y] = self.dg[y + x] = self.udg[self.n + y - x] = False
        self.path[x][y] = "."
