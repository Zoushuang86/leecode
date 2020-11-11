"""
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

"""
执行用时：68 ms, 在所有 Python3 提交中击败了83.89%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了10.76%的用户
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        else:
            i = 0
            j = 1
            max = 0
            while j < len(s):
                if s[j] in s[i:j]:
                    max = len(s[i:j]) if max < len(s[i:j]) else max
                    i = s.rindex(s[j], i, j) + 1
                j += 1
            return len(s[i:j]) if max < len(s[i:j]) else max


if __name__ == "__main__":
    s = "dvdf"
    print(Solution().lengthOfLongestSubstring(s))