"""
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。



示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""

"""
执行用时：5080 ms, 在所有 Python3 提交中击败了26.89%的用户
内存消耗：14.1 MB, 在所有 Python3 提交中击败了77.02%的用户
"""
class Solution1:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]


"""
执行用时：36 ms, 在所有 Python3 提交中击败了76.49%的用户
内存消耗：15.9 MB, 在所有 Python3 提交中击败了20.23%的用户
"""
class Solution:
    def twoSum(self, nums, target):
        hash_dict = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if hash_dict.get(temp) != None:
                return [hash_dict[temp], i]
            else:
                hash_dict[nums[i]] = i
        return [-1, -1]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))
