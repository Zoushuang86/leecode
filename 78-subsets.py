"""
78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。



示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]


提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同
"""
"""
方法一：库函数itertools
执行用时：40 ms, 在所有 Python3 提交中击败了57.46%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了21.06%的用户

class Solution:
    def subsets(self, nums):
        import itertools
        res = []
        for i in range(len(nums)+1):
            for temp in itertools.combinations(nums, i):
                res.append(list(temp))
        return res
"""
"""
方法二：迭代
执行用时：40 ms, 在所有 Python3 提交中击败了57.46%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.06%的用户

class Solution:
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            print(res)
            res = res+[num+[i] for num in res]
        return res
"""
"""
方法三：递归（回溯）
执行用时：48 ms, 在所有 Python3 提交中击败了12.55%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了15.00%的用户
"""
class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)

        def helper(i, temp):
            res.append(temp)
            for j in range(i, n):
                helper(j+1, temp + [nums[j]])
        helper(0, [])
        return res


if __name__ == "__main__":
    A = [1,2,3]
    s = Solution()
    print(s.subsets(A))
