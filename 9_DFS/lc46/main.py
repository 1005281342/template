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
