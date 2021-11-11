"""
47. 全排列 II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。


示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
class Solution:
    def permuteUnique(self, nums: list) -> list:
        nums.sort()
        res = []
        pre = []
        vis = [0] * len(nums)

        def dfs():
            if len(pre) == len(nums):
                res.append(pre[:])
                return

            for i in range(len(nums)):
                if vis[i] == 1:
                    continue
                if i > 0 and nums[i] == nums[i-1] and vis[i-1] == 0:
                    continue
                vis[i] = 1
                pre.append(nums[i])
                dfs()
                pre.pop()
                vis[i] = 0
        if len(nums) == 0:
            return res
        dfs()
        return res


if __name__ == "__main__":
    A = [0,1,0,1]
    s = Solution()
    print(s.permuteUnique(A))
