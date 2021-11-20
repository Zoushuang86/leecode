"""
416. 分割等和子集
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。



示例 1：

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。


提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100
通过次数185,691提交次数364,967
"""
class Solution:
    def canPartition(self, nums: list) -> bool:
        sumNums = sum(nums)
        if sumNums % 2:
            return False

        n = len(nums)
        capacity = sumNums // 2
        memo = [False for _ in range(capacity+1)]
        for i in range(capacity+1):
            memo[i] = (nums[0] == i)

        for i in range(1, n):
            for j in range(capacity, -1, -1):
                if j >= nums[i]:
                    memo[j] = (memo[j] or memo[j-nums[i]])
        return memo[capacity]


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    s = Solution()
    print(s.canPartition(nums))
