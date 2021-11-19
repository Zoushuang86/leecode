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


if __name__ == "__main__":
    weights = [1, 2, 3]
    values = [6, 10, 12]
    capacity = 5
    s = Solution()
    print(s.knapsack01(weights, values, capacity))
