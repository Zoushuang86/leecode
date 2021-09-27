"""
209. 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。



示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0


提示：

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105


进阶：

如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
"""

class Solution:
    """
    滑动窗口法：
    时间复杂度：O(n)
    空间复杂度：O(1)

    执行用时：48 ms, 在所有 Python3 提交中击败了41.28%的用户
    内存消耗：16.4 MB, 在所有 Python3 提交中击败了77.82%的用户
    """
    def minSubArrayLen(self, target, nums):
        left, right = 0, -1     # nums[left, right]为我们的滑动窗口
        sum = 0
        result = len(nums)+1
        while left < len(nums):
            if (sum < target) and (right+1<len(nums)):
                right += 1
                sum += nums[right]
            else:
                sum -= nums[left]
                left += 1
            if sum >= target:
                result = min(result, right-left+1)
        if result == len(nums)+1:
            return 0
        return result


if __name__ == "__main__":
    A = [2,7,11,15]
    target = 9
    s = Solution()
    print(s.minSubArrayLen(A, target))
