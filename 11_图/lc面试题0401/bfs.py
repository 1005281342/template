from typing import List
from collections import defaultdict, deque


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:

        dd = defaultdict(set)
        for a, b in graph:
            dd[a].add(b)

        dq = deque()
        dq.append(start)
        mark = set()
        while dq:
            node = dq.popleft()
            if node == target:
                return True

            if node in mark:
                continue

            dq.extend(dd[node])
            mark.add(node)

        return False
