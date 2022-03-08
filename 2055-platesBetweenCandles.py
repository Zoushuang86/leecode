"""
2055. 蜡烛之间的盘子
给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0 开始的字符串 s ，它只包含字符 '*' 和 '|' ，其中 '*' 表示一个 盘子 ，'|' 表示一支 蜡烛 。

同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] 表示 子字符串 s[lefti...righti] （包含左右端点的字符）。对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间 的盘子的 数目 。如果一个盘子在 子字符串中 左边和右边 都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。

比方说，s = "||**||**|*" ，查询 [3, 8] ，表示的是子字符串 "*||**|" 。子字符串中在两支蜡烛之间的盘子数目为 2 ，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。



示例 1:

ex-1

输入：s = "**|**|***|", queries = [[2,5],[5,9]]
输出：[2,3]
解释：
- queries[0] 有两个盘子在蜡烛之间。
- queries[1] 有三个盘子在蜡烛之间。
示例 2:

ex-2

输入：s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
输出：[9,0,0,0,0]
解释：
- queries[0] 有 9 个盘子在蜡烛之间。
- 另一个查询没有盘子在蜡烛之间。


提示：

3 <= s.length <= 105
s 只包含字符 '*' 和 '|' 。
1 <= queries.length <= 105
queries[i].length == 2
0 <= lefti <= righti < s.length
"""
"""
动态规划+预处理前缀
超时原因：只做了rights和lefts，没有做预处理前缀导致超时。与2195题超时原因差不多
lefts[i]：记录第i个盘子左侧最近的蜡烛下标，没有即为-1
rights[i]：记录第i个盘子右侧最近的蜡烛下标，没有即为n
plates[i]：记录第i个位置左侧盘子的总数
"""

class Solution:
    def platesBetweenCandles(self, s: str, queries: list) -> list:
        s = list(s)
        n = len(s)
        lefts = [0 for _ in range(n)]
        rights = [0 for _ in range(n)]
        plates = []
        left = -1
        right = n
        plate = 0
        for i in range(n):
            if s[i] == '|':
                left = i
            else:
                plate += 1
            lefts[i] = left
            plates.append(plate)

            if s[n - i - 1] == '|':
                right = n - i - 1
            rights[n - i - 1] = right

        res = []
        for l, r in queries:
            # 取出左边界右侧最近的蜡烛位置x，以及右边界左侧最近的蜡烛位置y
            x, y = rights[l], lefts[r]
            res.append(0 if x == n or y == -1 or x >= y else plates[y] - plates[x])
        return res

