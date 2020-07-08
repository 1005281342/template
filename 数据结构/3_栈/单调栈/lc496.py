from typing import List


class Solution:
    # 方法1
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stk, d = list(), dict()
        for num in nums2:
            # 找到右边第一个（后一个）比它大的数
            while stk and stk[-1] < num:
                d[stk.pop()] = num
            stk.append(num)
        return [d.get(num, -1) for num in nums1]
