"""
67. 二进制求和
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。



示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"


提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
"""

"""
执行用时：44 ms, 在所有 Python3 提交中击败了68.60%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.03%的用户
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = str(int(a) + int(b))
        result = list(result)
        index = len(result)-1
        real = ""
        while index >= 0:
            #print(result)
            if int(result[index]) > 1:
                if int(result[index]) == 2:
                    real = "0" + real
                else:
                    real = "1" + real
                if index != 0:
                    result[index-1] = str(int(result[index-1]) + 1)
                else:
                    real = "1" + real
            else:
                real = result[index] + real
            index -= 1
        return real

"""
执行用时：48 ms, 在所有 Python3 提交中击败了47.27%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了7.05%的用户
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        r, p = '', 0
        d = len(b) - len(a)
        a = '0' * d + a
        b = '0' * -d + b
        for i, j in zip(a[::-1], b[::-1]):
            s = int(i) + int(j) + p
            r = str(s % 2) + r
            p = s // 2
        return '1' + r if p else r

"""
执行用时：40 ms, 在所有 Python3 提交中击败了85.29%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了5.03%的用户
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print(Solution().addBinary(a, b))