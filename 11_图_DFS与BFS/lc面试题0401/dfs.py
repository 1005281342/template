from typing import List
from collections import defaultdict


class Solution:

    def __init__(self):
        self.dd = defaultdict(int)
        self.start = 0
        self.target = 0
        self.mark = set()
        self.ans = False

    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        self.dd = defaultdict(set)
        for a, b in graph:
            self.dd[a].add(b)
        self.start = start
        self.target = target

        return self.dfs(start)

    def dfs(self, node):

        if node == self.target:
            return True
        if node in self.mark:
            return False
        self.mark.add(node)
        for x in self.dd[node]:
            self.ans = self.ans or self.dfs(x)
        return self.ans
