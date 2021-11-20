"""
自顶向下递归

class Solution:
    memo = list()
    # 考虑用[0, index]的物品，填充容积为capacity的背包的最大价值
    def __bestVaule(self, weights, values, index, capacity) -> int:
        if index < 0 or capacity <= 0:
            return 0

        if self.memo[index][capacity] != -1:
            return self.memo[index][capacity]

        res = self.__bestVaule(weights, values, index-1, capacity)
        if capacity >= weights[index]:
            res = max(values[index] + self.__bestVaule(weights, values, index-1, capacity-weights[index]), res)
        self.memo[index][capacity] = res
        return res

    def knapsack01(self, weights: list, values:list, capacity: int) -> int:
        n = len(weights)
        self.memo = [[-1 for _ in range(capacity+1)] for _ in range(n)]
        return self.__bestVaule(weights, values, n-1, capacity)
"""

"""
动态优化

class Solution:
    def knapsack01(self, weights: list, values:list, capacity: int) -> int:
        n = len(weights)
        if n == 0:
            return 0

        f = [[-1] * (capacity + 1) for _ in range(n)]
        for j in range(capacity+1):
            f[0][j] = values[0] if j >= weights[0] else 0

        for i in range(1, n):
            for j in range(capacity+1):
                f[i][j] = f[i-1][j]
                if j >= weights[i]:
                    f[i][j] = max(f[i-1][j-weights[i]] + values[i], f[i][j])
        return f[-1][-1]
"""
"""
动态优化：空间优化两行数组

class Solution:
    def knapsack01(self, weights: list, values:list, capacity: int) -> int:
        n = len(weights)
        if n == 0:
            return 0

        f = [[-1] * (capacity + 1) for _ in range(2)]
        for j in range(capacity+1):
            f[0][j] = values[0] if j >= weights[0] else 0

        for i in range(1, n):
            for j in range(capacity+1):
                f[i%2][j] = f[(i-1)%2][j]
                if j >= weights[i]:
                    f[i%2][j] = max(f[(i-1)%2][j-weights[i]] + values[i], f[i%2][j])
        return f[(n-1)%2][capacity]
"""
"""
动态优化：空间优化一行数组
"""
class Solution:
    def knapsack01(self, weights: list, values:list, capacity: int) -> int:
        n = len(weights)
        if n == 0:
            return 0

        f = [-1 for _ in range((capacity + 1))]
        for i in range(capacity+1):
            f[i] = values[0] if i >= weights[0] else 0

        for i in range(1, n):
            for j in range(capacity, -1, -1):
                if j >= weights[i]:
                    f[j] = max(f[j-weights[i]] + values[i], f[j])
        return f[-1]


if __name__ == "__main__":
    weights = [1, 2, 3]
    values = [6, 10, 12]
    capacity = 5
    s = Solution()
    print(s.knapsack01(weights, values, capacity))
