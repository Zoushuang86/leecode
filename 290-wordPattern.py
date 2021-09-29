"""
290. 单词规律
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

输入: pattern = "abba", str = "dog cat cat dog"
输出: true
示例 2:

输入:pattern = "abba", str = "dog cat cat fish"
输出: false
示例 3:

输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
示例 4:

输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。
"""
"""
执行用时：28 ms, 在所有 Python3 提交中击败了86.19%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了46.68%的用户
"""
class Solution:
    def get_dict(self, s):
        res = ""
        i = 97
        s_dict = {}
        for e in s:
            if s_dict.get(e) == None:
                s_dict[e] = chr(i)
                res += chr(i)
                i += 1
            else:
                res += s_dict[e]
        return res

    def wordPattern(self, pattern: str, s: str) -> bool:
        p_dict = self.get_dict(list(pattern))
        s_dict = self.get_dict(s.split(" "))

        if p_dict == s_dict:
            return True
        else:
            return False


if __name__ == "__main__":
    A = "abba"
    p = "dog cat cat dog"
    s = Solution()
    print(s.wordPattern(A, p))