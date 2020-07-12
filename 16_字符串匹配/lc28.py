class Solution:

    def strStr(self, haystack: str, needle: str) -> int:

        if haystack == needle:
            return 0
        return self.KMP(haystack, needle)

    # 暴力做法
    def BF(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1

    # 利用Hash，HashCode相等的可能匹配，HashCode不等的一定不匹配
    def RK(self, haystack: str, needle: str) -> int:

        def get_code(strings: str) -> int:
            ans = 0
            for c in strings:
                ans += ord(c) - ord('a')
            return ans

        needle_code = get_code(needle)
        sub_haystack_code = get_code(haystack[:len(needle)])
        if needle_code == sub_haystack_code and needle == haystack[:len(needle)]:
            return 0

        for i in range(len(needle), len(haystack)):
            sub_haystack_code = sub_haystack_code - (ord(haystack[i - len(needle)]) - ord('a')) + (
                    ord(haystack[i]) - ord('a'))
            if needle_code == sub_haystack_code and haystack[i - len(needle) + 1:i + 1] == needle:
                return i - len(needle) + 1
        return -1

    # BM算法
    def BM(self, haystack: str, needle: str) -> int:

        # 坏字符失配移动表
        bad = dict()
        for i in range(len(needle)):
            bad[needle[i]] = i

        # 好后缀失配移动表
        # 情况1. 有子串匹配好后缀
        # 情况2. 好后缀无匹配，有最长前缀匹配好后缀的后缀
        # 情况3. 1，2都不成立

        # 构建suffix数组
        # i - q 为后缀字符串的长度， i 为匹配串的末位
        suffix = [len(needle)] * len(needle)
        for i in range(len(needle) - 2, -1, -1):
            q = i
            while q > 0 and needle[q] == needle[len(needle) - 1 - i + q]:
                q -= 1
            suffix[i] = i - q

        # 3 将needle字符串后移到第一位
        good = [len(needle)] * len(needle)
        # 2 若有最长前缀[0,i]匹配好后缀的后缀[len(needle)-1-i, len(needle)-1]，将ln-1-i之前的字符都可后移到ln-1-i处
        j = 0
        for i in range(len(needle) - 1, -1, -1):  # 从最长的前缀开始检索
            if suffix[i] == i + 1:  # 代表匹配到前缀的情况，q=-1
                while j < len(needle) - 1 - i:
                    if good[j] == len(needle):  # 未匹配的情况
                        good[j] = len(needle) - 1 - i
                    j += 1
        # 1 若有子串匹配好后缀，好后缀的左端点，j = len(needle)-1-suffix[i], 后移位数 len(needle)-1-i
        # 情况1，在情况2更新之后，保证了只移位到最后匹配的子串位置
        for i in range(len(needle) - 1):
            good[len(needle) - 1 - suffix[i]] = len(needle) - 1 - i

        i = 0
        while i <= len(haystack) - len(needle):
            j = len(needle) - 1
            while j > - 1 and haystack[i + j] == needle[j]:
                j -= 1
            if j < 0:
                return i
            move = bad.get(haystack[i + j], -1)  # 坏字符匹配，将needle字符串后移到坏字符出现的位置，若无，则到第一位
            i += max(good[j], j - move)
        return -1

    # KMP算法
    def KMP(self, haystack: str, needle: str) -> int:

        # 计算next数组
        ne = [0] * len(needle)
        if len(needle) > 0:
            ne[0] = -1

        i = 2
        j = 0
        while i < len(needle):
            if needle[i - 1] == needle[j]:
                j += 1
                ne[i] = j
                i += 1
            elif j > 0:
                j = ne[j]
            else:
                ne[i] = 0
                i += 1

        # 匹配
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif ne[j] == -1:
                i += 1
            else:
                j = ne[j]
        return i - j if j == len(needle) else -1


if __name__ == '__main__':
    S = Solution()
    # ans = S.strStr("hello", "ll")
    # print(ans)
    ans = S.strStr("mississippi", "pi")
    print(ans)
