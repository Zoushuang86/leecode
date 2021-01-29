"""
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""

"""
执行用时：60 ms, 在所有 Python3 提交中击败了50.78%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了14.92%的用户

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        else:
            sSet = set(s)
            tSet = set(t)
            if sSet != tSet:
                return False
            else:
                sDict = {}
                for item in s:
                    if item not in sDict:
                        sDict[item] = 1
                    else:
                        sDict[item] += 1
                tDict = {}
                for item in t:
                    if item not in tDict:
                        tDict[item] = 1
                    else:
                        tDict[item] += 1
                if sDict != tDict:
                        return False
                else:
                    return True
"""

"""
方法一：排序
t 是 ss 的异位词等价于「两个字符串排序后相等」
执行用时：60 ms, 在所有 Python3 提交中击败了50.78%的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了5.33%的用户
"""
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        else:
            return False

"""
方法二：算法包
执行用时：44 ms, 在所有 Python3 提交中击败了93.80%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了13.50%的用户
"""
import collections
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        d = collections.Counter(s)
        e = collections.Counter(t)
        return d == e


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    A = Solution()
    print(A.isAnagram(s, t))
