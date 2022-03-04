"""
剑指 Offer 53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。



示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0


提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums 是一个非递减数组
-109 <= target <= 109


注意：本题与主站 34 题相同（仅返回值不同）：
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""
class Solution:
    # 二分法：利用递增条件，O(logn)
    def search(self, nums: list, target: int) -> int:
        if len(nums) == 0:
            return 0

        left, right = 0, len(nums)-1

        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                break
        return right - left + 1 if nums[left] == target else 0


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 7
    s = Solution()
    print(s.search(nums, target))
