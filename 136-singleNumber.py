"""
136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4
"""

"""
执行用时：72 ms, 在所有 Python3 提交中击败了14.93%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了42.61%的用户

class Solution:
    def singleNumber(self, nums: list) -> int:
        nums = sorted(nums)
        if len(nums) == 1:
            return nums[0]
        elif nums[0] != nums[1]:
            return nums[0]
        elif nums[-1] != nums[-2]:
            return nums[-1]
        else:
            for index in range(1, len(nums)):
                if nums[index] != nums[index - 1] and nums[index] != nums[index + 1]:
                    return nums[index]
"""


"""
异或方法
异或运算有以下三个性质。

任何数和 00 做异或运算，结果仍然是原来的数，即 a⊕0=a。
任何数和其自身做异或运算，结果是 0，即 a⊕a=0。
异或运算满足交换律和结合律，即 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。

执行用时：72 ms, 在所有 Python3 提交中击败了14.93%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了82.70%的用户
"""
class Solution:
    def singleNumber(self, nums: list) -> int:
        result = 0
        for i in range(len(nums)):
            result = result ^ nums[i]
        return result


if __name__ == "__main__":
    s = [-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,-336,513,-560,-481,-174,101,-997,40,-527,-784,-283,354]
    print(Solution().singleNumber(s))
