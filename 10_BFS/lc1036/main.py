from typing import List
from bisect import insort, bisect_left
from collections import deque

MOVE = {(1, 0), (0, 1), (-1, 0), (0, -1)}


class Solution:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        if not blocked:
            return True

        x_all_nums = [0, source[0], 999999]
        y_all_nums = [0, source[1], 999999]
        for x, y in blocked:
            insort(x_all_nums, x)
            insort(y_all_nums, y)
        insort(x_all_nums, target[0])
        insort(y_all_nums, target[1])

        x_all_nums = self.unique(x_all_nums)
        y_all_nums = self.unique(y_all_nums)

        ns = (bisect_left(x_all_nums, source[0]), bisect_left(y_all_nums, source[1]))
        nt = (bisect_left(x_all_nums, target[0]), bisect_left(y_all_nums, target[1]))
        nbs = {(bisect_left(x_all_nums, x), bisect_left(y_all_nums, y)) for x, y in blocked}

        dq = deque()
        dq.append(ns)
        mark = {ns, }
        while dq:
            a, b = dq.popleft()
            for x, y in MOVE:
                x += a
                y += b
                if not (0 <= x < len(x_all_nums) and 0 <= y < len(y_all_nums)) or (x, y) in mark or (x, y) in nbs:
                    continue

                if x == nt[0] and y == nt[1]:
                    return True
                dq.append((x, y))
                mark.add((x, y))
        # if a == nt[0] and b == nt[1]:
        #     return True

        return False

    def unique(self, nums):
        if not nums:
            return nums
        ans = [nums[0]]
        for num in nums[1:]:
            if num != ans[-1]:
                ans.append(num)
        return ans


if __name__ == '__main__':
    # bs = [[100005, 100073], [100006, 100074], [100007, 100075], [100008, 100076], [100009, 100077],
    #       [100010, 100078], [100011, 100079], [100012, 100080], [100013, 100081], [100014, 100082],
    #       [100015, 100083], [100016, 100084], [100017, 100085], [100018, 100086], [100019, 100087],
    #       [100020, 100088], [100021, 100089], [100022, 100090], [100023, 100091], [100024, 100092],
    #       [100025, 100091], [100026, 100090], [100027, 100089], [100028, 100088], [100029, 100087],
    #       [100030, 100086], [100031, 100085], [100032, 100084], [100033, 100083], [100034, 100082],
    #       [100035, 100081], [100036, 100080], [100037, 100079], [100038, 100078], [100039, 100077],
    #       [100040, 100076], [100041, 100075], [100042, 100074], [100043, 100073], [100044, 100072],
    #       [100043, 100071], [100042, 100070], [100041, 100069], [100040, 100068], [100039, 100067],
    #       [100038, 100066], [100037, 100065], [100036, 100064], [100035, 100063], [100034, 100062],
    #       [100033, 100061], [100032, 100060], [100031, 100059], [100030, 100058], [100029, 100057],
    #       [100028, 100056], [100027, 100055], [100026, 100054], [100025, 100053], [100024, 100052],
    #       [100023, 100053], [100022, 100054], [100021, 100055], [100020, 100056], [100019, 100057],
    #       [100018, 100058], [100017, 100059], [100016, 100060], [100015, 100061], [100014, 100062],
    #       [100013, 100063], [100012, 100064], [100011, 100065], [100010, 100066], [100009, 100067],
    #       [100008, 100068], [100007, 100069], [100006, 100070], [100005, 100071]]
    # s = [100024, 100072]
    # t = [999994, 999990]

    bs = [[10, 9], [9, 10], [10, 11], [11, 10]]
    s = [0, 0]
    t = [10, 10]
    S = Solution()
    res = S.isEscapePossible(bs, s, t)
    print(res)
