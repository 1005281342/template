"""
原数组：[1, 2, 3, 4, 5, 6]
前缀和：[0, 1, 3, 6, 10, 15, 21]
"""


# 查找数组和
def search_sum(nums, lst):
    sums = [0] * (len(nums) + 1)
    # 查找前缀和
    for i in range(len(nums)):
        sums[i + 1] = sums[i] + nums[i]

    # 查找前缀和
    for left, right in lst:
        print(sums[right + 1] - sums[left])


# [和为K的子数组](https://leetcode-cn.com/problems/subarray-sum-equals-k/)
# 数据增强后O(N*N)已经过不了，Python版本
from typing import List
from collections import defaultdict


class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     sums = [0] * (len(nums) + 1)
    #     # 求前缀和
    #     for i in range(len(nums)):
    #         sums[i + 1] = sums[i] + nums[i]
    #
    #     cnt = 0
    #     # 查找前缀和
    #     for i in range(len(sums) - 1):
    #         for j in range(i + 1, len(sums)):
    #             if sums[j] - sums[i] == k:
    #                 cnt += 1
    #     return cnt

    # 使用Map进行优化（只适用于统计次数而不关心具体的解） 时间复杂度O(N)
    def subarraySum(self, nums: List[int], k: int) -> int:
        dd = defaultdict(int)
        sums = 0
        dd[sums] = 1
        cnt = 0
        for num in nums:
            sums += num
            cnt += dd[sums - k]
            dd[sums] += 1
        return cnt


if __name__ == '__main__':
    search_sum([1, 2, 3, 4, 5, 6], [(1, 3)])
