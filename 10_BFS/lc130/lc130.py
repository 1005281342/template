from typing import List
from collections import deque

MOVE = {
    (1, 0), (-1, 0),
    (0, 1), (0, -1),
}


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """ 
        方法1: 广度优先遍历
        第一次遍历：将边界'O'添加到队列中，将其能访问到且第一次被访问的'O'加到集合A（该集合中'O'不会被替换成'X'）
        第二次遍历：将不在A中的所有'O'替换成'X'
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return
        dq = deque()
        dq.extend([(0, j) for j in range(len(board[0])) if board[0][j] == 'O'])
        dq.extend([(len(board) - 1, j) for j in range(len(board[0])) if board[len(board) - 1][j] == 'O'])
        dq.extend([(i, 0) for i in range(len(board)) if board[i][0] == 'O'])
        dq.extend([(i, len(board[0]) - 1) for i in range(len(board)) if board[i][len(board[0]) - 1] == 'O'])

        s = set()
        while dq:
            node = dq.popleft()
            if node in s:
                continue
            s.add(node)
            i, j = node
            for x, y in MOVE:
                x += i
                y += j
                if (x < 0 or x >= len(board)) or (y < 0 or y >= len(board[0])):
                    continue
                if board[x][y] == 'O':
                    dq.append((x, y))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in s:
                    board[i][j] = 'X'
