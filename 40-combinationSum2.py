"""
40. 组合总和 II
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

注意：解集不能包含重复的组合。



示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]


提示:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
class Solution:
    res = []
    def __generate(self, candidates, start, target, pre, vis):
        if target == 0:
            self.res.append(pre[:])
            return

        for index in range(start, len(candidates)):
            if index > 0 and candidates[index-1] == candidates[index] and vis[index-1] == False:
                continue
            e = candidates[index]
            if target < e:
                break
            vis[index] = True
            self.__generate(candidates, index+1, target - e, pre+[e], vis)
            vis[index] = False

    def combinationSum2(self, candidates: list, target: int) -> list:
        self.res.clear()
        candidates.sort()
        vis = [False] * len(candidates)
        self.__generate(candidates, 0, target, [], vis)
        return self.res


if __name__ == "__main__":
    candidates = [2,5,2,1,2]
    target = 5
    s = Solution()
    print(s.combinationSum2(candidates, target))
