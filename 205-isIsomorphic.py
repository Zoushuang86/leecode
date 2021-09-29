"""
205. 同构字符串
给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。



示例 1:

输入：s = "egg", t = "add"
输出：true
示例 2：

输入：s = "foo", t = "bar"
输出：false
示例 3：

输入：s = "paper", t = "title"
输出：true


提示：

可以假设 s 和 t 长度相同。
"""
"""
执行用时：40 ms, 在所有 Python3 提交中击败了75.46%的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了5.12%的用户
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

    def isIsomorphic(self, s: str, t: str) -> bool:
        partten = self.get_dict(list(s))

        res = ""
        i = 97
        t_dict = {}
        for index, e in enumerate(t):
            if t_dict.get(e) == None:
                t_dict[e] = chr(i)
                res += chr(i)
                i += 1
            else:
                res += t_dict[e]
            if res[index] != partten[index]:
                return False
        return True


if __name__ == "__main__":
    A = "abba"
    p = "caac"
    s = Solution()
    print(s.isIsomorphic(A, p))