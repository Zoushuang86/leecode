"""
279. 完全平方数
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。



示例 1：

输入：n = 12
输出：3
解释：12 = 4 + 4 + 4
示例 2：

输入：n = 13
输出：2
解释：13 = 4 + 9

提示：

1 <= n <= 104
"""
"""
BFS无权图方法：
执行用时：476 ms, 在所有 Python3 提交中击败了82.64%的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了19.15%的用户

class Solution:
    def numSquares(self, n: int) -> int:
        queue = []  # [num, step]:num值，step走到num经过了几条路径
        queue.append([n, 0])

        # 排除存在推入相同数字的情况
        visited = [False for i in range(n+1)]
        visited[n] = True
        while len(queue) > 0:
            num = queue[0][0]
            step = queue[0][1]
            queue.pop(0)

            # 存在推入相同数字的情况
            for i in range(1, n+1):
                temp = num - i * i
                if temp < 0:
                    break
                if temp == 0:
                    return step + 1
                if visited[temp] == False:
                    queue.append([temp, step + 1])
                    visited[temp] = True
                i += 1
"""
"""
动态规划
"""
import math
class Solution:
    def numSquares(self, n: int) -> int:
        memo = [i for i in range(n + 1)]
        memo[1] = 1
        for i in range(2, n + 1):
            for j in range(1, int(math.sqrt(i)+1)):
                memo[i] = min(1+memo[i-j*j], memo[i])
        return memo[n]


if __name__ == "__main__":
    A = 13
    s = Solution()
    print(s.numSquares(A))
