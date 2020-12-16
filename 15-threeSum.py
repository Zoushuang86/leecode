"""
15. 三数之和
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。



示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def twoSum(self, nums, target):
        hash_dict = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in hash_dict.keys():
                return [hash_dict[temp], i]
            else:
                hash_dict[nums[i]] = i
        return [-1, -1]

    def threeSum(self, nums: list) -> list:
        results = []
        nums = sorted(nums)
        for k in range(len(nums)):
            temp = nums[k]
            nums.pop(k)
            index = self.twoSum(nums, -temp)
            nums.insert(k, temp)
            if -1 not in index:
                results.append([temp, nums[index[0]], nums[index[1]]])

        return results


if __name__ == "__main__":
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums1))