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
    """
    执行用时：124 ms, 在所有 Python3 提交中击败了17.77%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了88.75%的用户
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = list(s)
        freq = [0 for i in range(256)]  # 所有字符的ASCII码频率
        left, right = 0, -1     # 滑动窗口s[left, right]
        result = 0
        while left < len(arr):
            if (right+1 < len(arr)) and (freq[ord(arr[right+1])] == 0):
                right += 1
                freq[ord(arr[right])] += 1
            else:
                freq[ord(arr[left])] -= 1
                left += 1
            result = max(result, right-left+1)
        return result


if __name__ == "__main__":
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))