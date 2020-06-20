# [统计全为1的正方形子矩阵](https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/)
from typing import List


class Solution:
    # 超时O(N^3)
    def countSquares(self, matrix: List[List[int]]) -> int:
        x = len(matrix)
        if x == 0:
            return 0
        y = len(matrix[0])
        if y == 0:
            return 0

        sums = [[0 for _ in range(y + 1)] for _ in range(x + 1)]
        # 构造前缀和
        for i in range(x):
            for j in range(y):
                sums[i + 1][j + 1] = sums[i + 1][j] + sums[i][j + 1] - sums[i][j] + matrix[i][j]

        cnt = 0
        # 查找前缀和
        # 扫描所有正方形
        # 边长
        for length in range(1, min(x, y) + 1):
            for i in range(0, x - length + 1):
                for j in range(0, y - length + 1):
                    cnt += sums[i + length][j + length] - sums[i][j + length] - sums[i + length][j] + sums[i][
                        j] == length * length

        return cnt

        # 这道题需要使用DP进行解答，这里只是一个使用二维前缀和解答的例子
        # 从时间复杂度看（数据范围是0--300）, 对于O(N^3)则数据量级达27000000，Python版本可能会超时，使用go不会
        # go版本见同目录下的lc1277
