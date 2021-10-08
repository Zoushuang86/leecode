"""
49. 字母异位词分组
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母都恰好只用一次。



示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:

输入: strs = [""]
输出: [[""]]
示例 3:

输入: strs = ["a"]
输出: [["a"]]


提示：

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母
"""
"""
执行用时：2796 ms, 在所有 Python3 提交中击败了5.04%的用户
内存消耗：19.9 MB, 在所有 Python3 提交中击败了5.19%的用户

class Solution:
    def groupAnagrams(self, strs):
        group = []
        res = []
        def getMode(string):
            mode = [0] * 26
            for s in string:
                mode[ord(s)-ord('a')] += 1
            return mode
        for string in strs:
            mode = getMode(string)
            if mode not in group:
                group.append(mode)
                res.append([])

            res[group.index(mode)].append(string)
        return res
"""

# 将mode编码成str进行hash
"""
执行用时：68 ms, 在所有 Python3 提交中击败了18.42%的用户
内存消耗：18.8 MB, 在所有 Python3 提交中击败了23.03%的用户
"""
class Solution:
    def groupAnagrams(self, strs):
        index = 0
        group = {}
        res = []
        def getMode(string):
            mode = [0] * 26
            for s in string:
                mode[ord(s)-ord('a')] += 1
            return str(mode)

        for string in strs:
            mode = getMode(string)
            if group.get(mode) == None:
                group[mode] = index
                index += 1
                res.append([])

            res[group.get(mode)].append(string)
        return res


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
