"""
268. 丢失的数字
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。



进阶：

你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?


示例 1：

输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
示例 2：

输入：nums = [0,1]
输出：2
解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。
示例 3：

输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。
示例 4：

输入：nums = [0]
输出：1
解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。


提示：

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
nums 中的所有数字都 独一无二
"""

"""
方法一：
执行用时：48 ms, 在所有 Python3 提交中击败了72.44%的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了7.89%的用户

class Solution:
    def missingNumber(self, nums):
        length = len(nums)
        flags = [False] * (length+1)
        for num in nums:
            flags[num] = True
        return flags.index(False)
"""

"""
方法二：求和差值法
执行用时：40 ms, 在所有 Python3 提交中击败了94.09%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了18.37%的用户
"""
class Solution:
    def missingNumber(self, nums):
        return sum(range(len(nums)+1)) - sum(nums)

"""
方法三：排序比较法
执行用时：56 ms, 在所有 Python3 提交中击败了45.49%的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了7.17%的用户

class Solution:
    def missingNumber(self, nums):
        nums = sorted(nums)
        for index in range(len(nums)):
            if index != nums[index]:
                return index
        return len(nums)
"""


if __name__ == "__main__":
    A = [0,1]
    s = Solution()
    print(s.missingNumber(A))