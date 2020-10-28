"""
66. 加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""

"""
执行用时：36 ms, 在所有 Python3 提交中击败了87.79%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了12.70%的用户
"""

class Solution:
    def plusOne(self, digits):
        index = len(digits) - 1
        digits[index] += 1
        while index > 0:
            if digits[index] == 10:
                digits[index-1] += 1
                digits[index] = 0
                index -= 1
            else:
                break
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    s = [9, 8, 9]
    print(Solution().plusOne(s))


