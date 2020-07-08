from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stk = list()

        nums2 = nums + nums

        for i, num in enumerate(nums2):

            # 找到第i个数的下一个比它大的元素
            while stk and nums[stk[-1]] < num:
                ans[stk.pop()] = num

            # 这里需要判断所维护的单调栈是否重复添加nums中的元素
            if i < len(nums):
                stk.append(i)

        return ans
