from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        ans = 0
        stk = list()
        for i in range(len(height)):
            while stk and height[stk[-1]] < height[i]:
                ti = stk.pop()
                while stk and height[stk[-1]] == height[ti]:
                    stk.pop()
                if stk:
                    ans += (i - stk[-1] - 1) * (min(height[stk[-1]], height[i]) - height[ti])

            stk.append(i)

        return ans
