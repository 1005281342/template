from typing import List
from collections import deque

MOVE = {
    (1, 1),  # 右下角移动
    (1, 0), (0, 1),
    (-1, 1), (1, -1),
    (-1, 0), (0, -1),
    (-1, -1),
}


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # 如果起点就阻塞
        if grid[0][0] or grid[-1][-1]:
            return -1

        dq = deque()
        dq.append((0, 0, 1))
        mark = {(0, 0), }
        while dq:
            a, b, d = dq.popleft()
            for x, y in MOVE:
                x += a
                y += b

                if x == len(grid) - 1 and y == len(grid) - 1:
                    return d + 1

                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in mark and not grid[x][y]:
                    mark.add((x, y))
                    dq.append((x, y, d + 1))

        # 队列中的最后一个点就是目标值时
        if a == len(grid) - 1 and b == len(grid) - 1:
            return d

        return -1
