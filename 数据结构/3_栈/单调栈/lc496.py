from typing import List


class Solution:
    # 方法1
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stk, d = list(), dict()
        for num in nums2:
            while stk and stk[-1] < num:
                d[stk.pop()] = num
            stk.append(num)
        return [d.get(num, -1) for num in nums1]

    # 方法2
    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = [-1] * len(nums1)

        d = dict()
        for i, num in enumerate(nums1):
            d[num] = i

        stk = list()
        # 查找右边第一个比它大的数，若将数组反转则转化为求反转数组左边第一个比它大的数
        for num in nums2[::-1]:
            if not stk:
                stk.append(num)
                continue
            while stk and stk[-1] < num:
                stk.pop()

            if stk:
                if d.get(num) is None:
                    stk.append(num)
                    continue
                ans[d[num]] = stk[-1]
            stk.append(num)

        return ans

