from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = [0] * len(nums)
        left = 0
        right = -1
        ans = list()
        for i in range(len(nums)):
            # 此处也可以写成if, 因此每次滑动只会前进一步
            while left <= right and i - k + 1 > dq[left]:
                left += 1
            while left <= right and nums[dq[right]] <= nums[i]:
                right -= 1
            right += 1
            dq[right] = i

            if i >= k - 1:
                ans.append(nums[dq[left]])
        # print(dq)
        return ans

    # 求滑动窗口中的最小值
    def minSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = list()
        left = 0
        right = - 1
        dq = [0] * len(nums)
        for i in range(len(nums)):

            # 如果所维护的窗口大小已经超过k则弹出最左边的元素
            while left <= right and i - k + 1 > dq[left]:
                left += 1

            # nums[i]是局部最小值，将其前面比它大的值都移除
            while left <= right and nums[dq[right]] >= nums[i]:
                right -= 1

            right += 1
            dq[right] = i

            if i >= k - 1:
                ans.append(nums[dq[left]])
        # print(dq)
        return ans


if __name__ == '__main__':
    S = Solution()
    res = S.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print(res)
    res = S.minSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print(res)
