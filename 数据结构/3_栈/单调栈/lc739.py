from typing import List

"""
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。
如果气温在这之后都不会升高，请在该位置用 0 来代替。
例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
"""
"""
分析：找到下一个比当前元素a值大的元素b，b_idx - a_idx即为所求
"""


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stk = list()
        for i, num in enumerate(T):
            while stk and T[stk[-1]] < num:
                # 在右边找到了第一个比"当前位置"T[stk[-1]]大的元素
                ti = stk.pop()
                ans[ti] = i - ti
            stk.append(i)
        return ans
