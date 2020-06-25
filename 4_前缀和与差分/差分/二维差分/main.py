class Solution(object):

    def __init__(self, matrix):
        self.m = len(matrix) + 1
        self.n = len(matrix[0]) + 1

        x = len(matrix) + 10
        y = len(matrix[0]) + 10
        self.nums = [[0] * y for _ in range(x)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.add(i + 1, j + 1, i + 1, j + 1, matrix[i][j])

    def add(self, x1, y1, x2, y2, c):
        self.nums[x1][y1] += c
        self.nums[x2 + 1][y1] -= c
        self.nums[x1][y2 + 1] -= c
        self.nums[x2 + 1][y2 + 1] += c

    def query(self):
        ans = [[0] * self.n for _ in range(self.m)]
        for i in range(1, self.m):
            for j in range(1, self.n):
                ans[i][j] = ans[i][j - 1] + ans[i - 1][j] - ans[i - 1][j - 1] + self.nums[i][j]
        print(ans)


if __name__ == '__main__':
    S = Solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    S.add(1, 1, 2, 2, 100)
    S.query()
