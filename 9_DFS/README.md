---
title: DFS(深度优先遍历)
---

### 全排列问题
[LeetCode](https://leetcode-cn.com/problems/permutations/)

```python
# https://leetcode-cn.com/problems/permutations/
from typing import List


class Solution:

    def __init__(self):
        self.nums = list()
        self.ans = list()
        self.path = list()
        self.st = list()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.ans = list()
        self.st = [False] * len(nums)
        self.path = [0] * len(nums)

        self.dfs(0)
        return self.ans

    def dfs(self, u: int):
        if u == len(self.nums):
            # 进行拷贝
            self.ans.append(self.path[:])
            return
        for i in range(len(self.nums)):
            # 说明已经用过了
            if self.st[i]:
                continue

            # 选择
            self.path[u] = self.nums[i]
            self.st[i] = True
            self.dfs(u + 1)
            # 回溯
            self.st[i] = False
            # self.path[u] = 0  # 其实每次都会在在选择时被nums[i]覆盖，不恢复path[u]也可以

```

### N皇后问题

[LeetCode](https://leetcode-cn.com/problems/n-queens/)

```python
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
```

**一种更原始的做法**

```python
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
```

