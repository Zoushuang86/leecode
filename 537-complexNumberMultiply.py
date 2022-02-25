"""
537. 复数乘法
复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：

实部 是一个整数，取值范围是 [-100, 100]
虚部 也是一个整数，取值范围是 [-100, 100]
i2 == -1
给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。



示例 1：

输入：num1 = "1+1i", num2 = "1+1i"
输出："0+2i"
解释：(1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。
示例 2：

输入：num1 = "1+-1i", num2 = "1+-1i"
输出："0+-2i"
解释：(1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。


提示：

num1 和 num2 都是有效的复数表示。
"""
class Solution:
    """
    执行用时：40 ms, 在所有 Python3 提交中击败了22.15%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了15.19%的用
    """
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = int(num1.split('+')[0]), int(num1.split('+')[-1][:-1])
        c, d = int(num2.split('+')[0]), int(num2.split('+')[-1][:-1])
        p = a * c - b * d
        q = a * d + b * c
        return str(p) + "+" + str(q) + "i"


if __name__ == "__main__":
    num1 = "1+1i"
    num2 = "1+-3i"
    s = Solution()
    print(s.complexNumberMultiply(num1, num2))
