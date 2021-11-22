"""
494. 目标和
给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。



示例 1：

输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
示例 2：

输入：nums = [1], target = 1
输出：1


提示：

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
"""
class Solution:
    def findTargetSumWays(self, nums: list, target: int) -> int:
        sumNums = sum(nums)
        if abs(target) > abs(sumNums):
            return 0

        n = len(nums)
        length = 2 * sumNums + 1
        dp = [[0 for _ in range(length)] for _ in range(n)]
        # 加上sum是因为下标是从-sumNums到sumNums
        dp[0][sumNums + nums[0]] += 1
        dp[0][sumNums - nums[0]] += 1
        for i in range(1, n):
            for j in range(-sumNums, sumNums+1):
                if j+nums[i] > sumNums:
                    dp[i][j+sumNums] = dp[i-1][j-nums[i]+sumNums]
                elif j-nums[i] < -sumNums:
                    dp[i][j+sumNums] = dp[i-1][j+nums[i]+sumNums]
                else:
                    dp[i][j+sumNums] = dp[i-1][j-nums[i]+sumNums] + dp[i-1][j+nums[i]+sumNums]
        return dp[n-1][target+sumNums]


if __name__ == "__main__":
    nums = [1,1,1,1,1]
    target = 3
    solution = Solution()
    print(solution.findTargetSumWays(nums, target))

