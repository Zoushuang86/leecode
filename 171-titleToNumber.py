"""
171. Excel表列序号
给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
示例 1:

输入: "A"
输出: 1
示例 2:

输入: "AB"
输出: 28
示例 3:

输入: "ZY"
输出: 701
"""
"""
执行用时：52 ms, 在所有 Python3 提交中击败了10.63%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了6.98%的用户

class Solution:
    def titleToNumber(self, s: str) -> int:
        dictList = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = 0
        n = 0
        for e in s[::-1]:
            res += dictList.index(e) * (26 ** n)
            n += 1
        return res
"""

"""
执行用时：48 ms, 在所有 Python3 提交中击败了23.00%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了35.55%的用户
"""
class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        n = 0
        sdict = {}
        for i in range(1, 27):
            sdict[chr(i + 64)] = i
        for e in s[::-1]:
            res += sdict[e] * (26 ** n)
            n += 1
        return res


"""
执行用时：56 ms, 在所有 Python3 提交中击败了10.63%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了10.83%的用户

class Solution:
    def titleToNumber(self, s: str) -> int:
        d = len(s)
        value = 0
        sdict = {}
        for i in range(1, 27):
            sdict[chr(i+64)] = i
        for i in s:
            if d > 0:
                value += sdict[i] * 26**(d-1)
                d -= 1
        return value
"""


if __name__ == "__main__":
    s = "AAA"
    A = Solution()
    print(A.titleToNumber(s))