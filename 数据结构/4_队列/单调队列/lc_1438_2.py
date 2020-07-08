from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_dq, min_dq = deque(), deque()
        max_len = 0
        left = 0
        for right, num in enumerate(nums):
            while max_dq and num > max_dq[-1]:
                max_dq.pop()
            max_dq.append(num)
            while min_dq and num < min_dq[-1]:
                min_dq.pop()
            min_dq.append(num)

            # max_dq[0]是当前窗口最大值
            # min_dq[0]是当前窗口最小值
            while max_dq[0] - min_dq[0] > limit:
                # 窗口内不满足差值<=limit，从窗口左端开始丢弃值
                if nums[left] == max_dq[0]:
                    max_dq.popleft()
                if nums[left] == min_dq[0]:
                    min_dq.popleft()
                left += 1
            if max_dq[0] - min_dq[0] <= limit:
                max_len = max(max_len, right - left + 1)
        return max_len
