"""
387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2


提示：你可以假定该字符串只包含小写字母。
"""
"""
执行用时：5808 ms, 在所有 Python3 提交中击败了5.04%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了30.51%的用户

class Solution:
    def firstUniqChar(self, s):
        for item in s:
            if s.count(item) == 1:
                return s.index(item)
        return -1
"""

"""
执行用时：140 ms, 在所有 Python3 提交中击败了38.35%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了17.61%的用户
"""
class Solution:
    def firstUniqChar(self, s):
        charDict = {}
        for item in s:
            if item not in charDict:
                charDict[item] = 1
            else:
                charDict[item] += 1
        for index in range(len(s)):
            if charDict[s[index]] == 1:
                return index
        return -1


"""
执行用时：96 ms, 在所有 Python3 提交中击败了81.50%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了23.37%的用户
class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = collections.Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1
"""

if __name__ == "__main__":
    A = "loveleetcode"
    s = Solution()
    print(s.firstUniqChar(A))
