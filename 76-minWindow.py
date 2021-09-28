"""
76. 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。


示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。

提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成

进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
"""

import collections

class Solution:
    """
    执行用时: 1208 ms
    内存消耗: 15.3 MB
    """
    def check(self, s_cnt, t_cnt):
        for i in range(len(t_cnt)):
            if t_cnt[i] > s_cnt[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        min_len = n + 1
        res = ""

        if n < m:
            return ""
        s_cnt = [0] * 59
        t_cnt = [0] * 59
        for e in t:
            t_cnt[ord(e)-ord('A')] += 1

        left, right = 0, -1
        while left < n-m+1:
            if (self.check(s_cnt, t_cnt) == False) and (right+1 < n):
                right += 1
                print(ord(s[right]) - ord('A'))
                s_cnt[ord(s[right]) - ord('A')] += 1
            else:
                s_cnt[ord(s[left]) - ord('A')] -= 1
                left += 1

            if self.check(s_cnt, t_cnt):
                if min_len > right - left + 1:
                    res = s[left:right + 1]
                    min_len = right - left + 1
        return res
    # TODO: 优化存储判断


if __name__ == "__main__":
    A = "ADOBECODEBANC"
    p = "ABC"
    s = Solution()
    print(s.minWindow(A, p))
