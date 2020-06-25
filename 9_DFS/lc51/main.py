# https://leetcode-cn.com/problems/n-queens/
from typing import List


class Solution:

    def __init__(self):
        self.n = 0
        self.x = list()  # 竖行
        self.dg = list()  # 左对角线: y = - x + b -> b = x + y
        self.udg = list()  # 右对角线: y = x + b -> b = y - x
        self.ans = list()
        self.path = list()

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.x = [False] * n * 2
        self.dg = [False] * n * 2
        self.udg = [False] * n * 2
        self.path = [['.'] * n for _ in range(n)]

        self.dfs(0)
        return self.ans

    def dfs(self, u):
        if u == self.n:
            self.ans.append(["".join(x) for x in self.path])
            return

        for i in range(self.n):
            if self.x[i] or self.dg[u + i] or self.udg[self.n + i - u]:
                continue
            self.path[u][i] = 'Q'
            self.x[i] = self.dg[u + i] = self.udg[self.n + i - u] = True
            self.dfs(u + 1)
            self.x[i] = self.dg[u + i] = self.udg[self.n + i - u] = False
            self.path[u][i] = '.'
