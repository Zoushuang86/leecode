"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
"""

"""
执行用时：56 ms, 在所有 Python3 提交中击败了9.78%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.29%的用户
"""
"""
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 0:
            return ""
        else:
            t = ''
            min_len = min([len(strs[0]), len(strs[1])])
            for i in range(min_len):
                if strs[0][i] == strs[1][i]:
                    t += strs[0][i]
                else:
                    break
            if len(t) == 0:
                return ""
            else:
                return self.longestCommonPrefix(strs[2:] + [t])
"""

"""
执行用时：36 ms, 在所有 Python3 提交中击败了93.09%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.29%的用户
"""
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        str0 = min(strs)
        str1 = max(strs)
        print(str0, str1)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0


if __name__ == "__main__":
    x = ["zcd","z","aa"]
    s = Solution()
    print(s.longestCommonPrefix(x))


