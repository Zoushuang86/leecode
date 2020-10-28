"""
58. 最后一个单词的长度
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。



示例:

输入: "Hello World"
输出: 5
"""

"""
执行用时：44 ms, 在所有 Python3 提交中击败了41.13%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了15.95%的用户

class Solution:
    def lengthOfLastWord(self, s):
        return len(s.strip(" ").split(" ")[-1])
"""
"""
执行用时：40 ms, 在所有 Python3 提交中击败了66.72%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.11%的用户
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        needle = len(s) - 1
        length = 0
        for char in s[::-1]:
            if char == " ":
                needle -= 1
            else:
                break
        while needle >= 0:
            char = s[needle]
            if char == " ":
                break
            else:
                length += 1
            needle -= 1
        return length


if __name__ == "__main__":
    s = "Hello World "
    print(Solution().lengthOfLastWord(s))
