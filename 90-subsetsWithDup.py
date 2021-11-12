"""
90. 子集 II
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。



示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]


提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
class Solution:
    def subsetsWithDup(self, nums: list) -> list:
        res = []
        nums.sort()
        n = len(nums)
        vis = [False] * n

        def helper(i, temp):
            res.append(temp)
            for j in range(i, n):
                if j >0 and nums[j] == nums[j-1] and vis[j-1] == False:
                    continue
                vis[j] = True
                helper(j + 1, temp + [nums[j]])
                vis[j] = False

        helper(0, [])
        return res


if __name__ == "__main__":
    A = [1,2,2]
    s = Solution()
    print(s.subsetsWithDup(A))
