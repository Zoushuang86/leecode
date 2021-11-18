"""
198. 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。



示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。


提示：

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
"""
# 自顶向下递归
class Solution:
    memo = list()

    # 考虑抢劫nums[index, len(nums))范围的所有房子
    def __tryRob(self, nums, index):
        n = len(nums)
        if index >= n:
            return 0

        if self.memo[n] != -1:
            return self.memo[n]

        res = 0
        for i in range(index, n):
            res = max(nums[i] + self.__tryRob(nums, i+2), res)
        self.memo[i] = res
        return res

    def rob(self, nums: list) -> int:
        self.memo = [-1 for _ in range(len(nums)+1)]
        return self.__tryRob(nums, 0)
"""
"""
# 动态规划1
class Solution:
    def rob(self, nums: list) -> int:
        n = len(nums)
        if n == 0:
            return 0

        memo = [-1 for _ in range(len(nums))]
        memo[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            for j in range(i, n):
                memo[i] = max(memo[i], nums[j] + (memo[j+2] if j+2 < n else 0))
        return memo[0]
"""

# 动态规划2
class Solution:
    def rob(self, nums: list) -> int:
        n = len(nums)
        if n == 0:
            return 0

        memo = [-1 for _ in range(len(nums)+1)]
        memo[0], memo[1] = 0, nums[0]
        for i in range(2, n+1):
            memo[i] = max(memo[i-1], memo[i-2]+nums[i-1])
        return memo[-1]


if __name__ == "__main__":
    nums = [2,7,9,3,1]
    s = Solution()
    print(s.rob(nums))
