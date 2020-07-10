from typing import List
import bisect


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = j = 0
        st = []
        ans = 0
        while j < len(nums):
            bisect.insort(st, nums[j])
            while st[-1] - st[0] > limit:
                st.remove(nums[i])
                i += 1
            j += 1
            ans = max(ans, len(st))
        return ans
