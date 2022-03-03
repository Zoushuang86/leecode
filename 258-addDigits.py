"""
258. 各位相加
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

示例 1:

输入: num = 38
输出: 2
解释: 各位相加的过程为：
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
由于 2 是一位数，所以返回 2。
示例 1:

输入: num = 0
输出: 0


提示：

0 <= num <= 231 - 1


进阶：你可以不使用循环或者递归，在 O(1) 时间复杂度内解决这个问题吗？

通过次数92,906提交次数133,517
"""
class Solution:
    """
    方法一：模拟

    def addDigits(self, num: int) -> int:
        while num > 9:
            temp = 0
            while num > 0:
                temp += num % 10
                num //= 10
            num = temp
        return num
    """
    """
    方法二：数学归纳法
    https://blog.csdn.net/weixin_41541562/article/details/106635899
    """
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num else 0


if __name__ == "__main__":
    string = 119
    s = Solution()
    print(s.addDigits(string))
