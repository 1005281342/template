from typing import List
from collections import defaultdict, deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        dd = defaultdict(set)
        dc = defaultdict(int)
        for a, b in prerequisites:
            dd[b].add(a)
            dc[a] += 1

        dq = deque()
        dq.extend([i for i in range(numCourses) if dc[i] == 0])
        mark = set()
        while dq:
            node = dq.popleft()
            if node in mark:
                continue
            mark.add(node)

            for t in dd[node]:
                dc[t] -= 1
                if dc[t] == 0:
                    dq.append(t)

        return len(mark) == numCourses
