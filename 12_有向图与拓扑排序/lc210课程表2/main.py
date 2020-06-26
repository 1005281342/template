from typing import List
from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        dd = defaultdict(set)
        dc = defaultdict(int)
        for a, b in prerequisites:
            dd[b].add(a)
            dc[a] += 1

        dq = deque()
        dq.extend([i for i in range(numCourses) if dc[i] == 0])
        mark = set()
        ans = list()
        while dq:
            node = dq.popleft()
            if node in mark:
                continue
            mark.add(node)
            ans.append(node)

            for t in dd[node]:
                dc[t] -= 1
                if dc[t] == 0:
                    dq.append(t)

        if len(mark) == numCourses:
            return ans
        return list()
