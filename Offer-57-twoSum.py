"""
剑指 Offer 57. 和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：

输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]


限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
"""
# 哈希法
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        if len(nums) == 1:
            return []
        s = set(nums)
        for e in nums:
            if target-e in s:
                return [e, target-e]
        return []

# 双指针+二分查找
class Solution:
    def isExist(self, left, right, nums, target):
        while left <= right:
            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return False

    def twoSum(self, nums: list, target: int) -> list:
        n = len(nums)
        if n == 1:
            return []
        for i in range(n-1):
            val = target-nums[i]
            if nums[i+1] <= val <= nums[-1]:
                if self.isExist(i+1, n-1, nums, val):
                    return [nums[i], val]
        return []