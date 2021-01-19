"""
121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。

注意：你不能在买入股票前卖出股票。



示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

"""
方法一：暴力破解法
超时
复杂度分析
时间复杂度：O(n^2)。循环运行n*(n-1)/2次。
空间复杂度：O(1)。只使用了常数个变量。

class Solution:
    def maxProfit(self, prices):
        result = 0
        for index in range(len(prices)-1):
            for day in range(1, len(prices)-index):
                profit = prices[index+day] - prices[index]
                if profit > result:
                    result = profit
        return result
"""

"""
方法二：一次遍历
遍历一遍数组，计算每次 到当天为止 的最小股票价格和最大利润。
复杂度分析
时间复杂度：O(n)，遍历了一遍数组。
空间复杂度：O(1)，使用了有限的变量。

执行用时：268 ms, 在所有 Python3 提交中击败了12.29%的用户
内存消耗：23.4 MB, 在所有 Python3 提交中击败了5.00%的用户

class Solution:
    def maxProfit(self, prices):
        minPrice = float('inf')
        maxProfit = 0
        for price in prices:
            minPrice = min(price, minPrice)
            maxProfit = max(price - minPrice, maxProfit)
        return maxProfit
"""
"""
方法三：动态规划
动态规划一般分为一维、二维、多维（使用状态压缩），对应形式为 dp(i)、dp(i)(j)、二进制dp(i)(j)。

1. 动态规划做题步骤
明确 dp(i) 应该表示什么（二维情况：dp(i)(j)）；
根据 dp(i) 和 dp(i-1) 的关系得出状态转移方程；
确定初始条件，如 dp(0)。

2. 本题思路
其实方法二的思路不是凭空想象的，而是由动态规划的思想演变而来，优化了空间复杂度。
这里介绍一维动态规划思想。
dp[i] 表示前 i 天的最大利润，因为我们始终要使利润最大化，则：
dp[i] = max(dp[i-1], prices[i]-minPrice)

复杂度分析
时间复杂度：O(n)。
空间复杂度：O(n)。

执行用时：352 ms, 在所有 Python3 提交中击败了10.59%的用户
内存消耗：23.6 MB, 在所有 Python3 提交中击败了5.00%的用户
"""
class Solution:
    def maxProfit(self, prices):
        length = len(prices)
        # 边界条件
        if length == 0:
            return 0
        dp = [0] * length
        minPrice = prices[0]

        for i in range(1, length):
            minPrice = min(minPrice, prices[i])
            dp[i] = max(dp[i-1], prices[i]-minPrice)

        return dp[-1]


if __name__ == "__main__":
    A = [7,1,5,3,6,4]
    s = Solution()
    print(s.maxProfit(A))
