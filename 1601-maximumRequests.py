"""
1601. 最多可达成的换楼请求数目
我们有 n 栋楼，编号从 0 到 n - 1 。每栋楼有若干员工。由于现在是换楼的季节，部分员工想要换一栋楼居住。

给你一个数组 requests ，其中 requests[i] = [fromi, toi] ，表示一个员工请求从编号为 fromi 的楼搬到编号为 toi 的楼。

一开始 所有楼都是满的，所以从请求列表中选出的若干个请求是可行的需要满足 每栋楼员工净变化为 0 。意思是每栋楼 离开 的员工数目 等于 该楼 搬入 的员工数数目。比方说 n = 3 且两个员工要离开楼 0 ，一个员工要离开楼 1 ，一个员工要离开楼 2 ，如果该请求列表可行，应该要有两个员工搬入楼 0 ，一个员工搬入楼 1 ，一个员工搬入楼 2 。

请你从原请求列表中选出若干个请求，使得它们是一个可行的请求列表，并返回所有可行列表中最大请求数目。



示例 1：



输入：n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
输出：5
解释：请求列表如下：
从楼 0 离开的员工为 x 和 y ，且他们都想要搬到楼 1 。
从楼 1 离开的员工为 a 和 b ，且他们分别想要搬到楼 2 和 0 。
从楼 2 离开的员工为 z ，且他想要搬到楼 0 。
从楼 3 离开的员工为 c ，且他想要搬到楼 4 。
没有员工从楼 4 离开。
我们可以让 x 和 b 交换他们的楼，以满足他们的请求。
我们可以让 y，a 和 z 三人在三栋楼间交换位置，满足他们的要求。
所以最多可以满足 5 个请求。
示例 2：



输入：n = 3, requests = [[0,0],[1,2],[2,1]]
输出：3
解释：请求列表如下：
从楼 0 离开的员工为 x ，且他想要回到原来的楼 0 。
从楼 1 离开的员工为 y ，且他想要搬到楼 2 。
从楼 2 离开的员工为 z ，且他想要搬到楼 1 。
我们可以满足所有的请求。
示例 3：

输入：n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
输出：4


提示：

1 <= n <= 20
1 <= requests.length <= 16
requests[i].length == 2
0 <= fromi, toi < n
"""
class Solution:
    """
    方法一：回溯法+枚举

    我们可以通过回溯的方式枚举每一个请求是否被选择。

    定义函数 dfs(pos) 表示我们正在枚举第 pos 个请求。同时，我们使用数组 delta 记录每一栋楼的员工变化量，
    以及变量 cnt 记录被选择的请求数量。

    对于第 pos 个请求 [x,y]，如果选择该请求，那么就需要将 delta[x] 的值减 1，delta[y] 的值加 1，cnt 的值加 1；
    如果不选择该请求，则不需要进行任何操作。在这之后，我们调用 dfs(pos+1) 枚举下一个请求。
    如果我们枚举完了全部请求，则需要判断是否满足要求，也就是判断 delta 中的所有值是否均为 0。若满足要求，则更新答案的最大值。

    代码实现时，可以在修改 delta 的同时维护 delta 中的 0 的个数，记作 zero，初始值为 nn。如果 delta[x] 增加或减少前为 0，
    则将 zero 减 1；如果 delta[x] 增加或减少后为 0，则将 zero 加 1。

    复杂度分析
    · 时间复杂度：O(2^m)，其中 m 是数组 requests 的长度，即请求的数量。从 m 个请求中任意选择请求的方案数为 2^m，
    对于每一种方案，我们需要 O(1) 的时间判断其是否满足要求。
    · 空间复杂度：O(m+n)。递归需要 O(m) 的栈空间，数组 delta 需要 O(n) 的空间。
    """
    def maximumRequests(self, n: int, requests: list) -> int:
        delta = [0] * n
        res, cnt, zero = 0, 0, n

        def dfs(pos: int) -> None:
            nonlocal res, cnt, zero
            if pos == len(requests):
                if zero == n:
                    res = max(res, cnt)
                return

            # 不选中requests[pos]
            dfs(pos+1)

            # 选中requests[pos]
            z = zero
            cnt += 1
            x, y = requests[pos]
            zero -= delta[x] == 0
            delta[x] -= 1
            zero += delta[x] == 0
            zero -= delta[y] == 0
            delta[y] += 1
            zero += delta[y] == 0
            dfs(pos+1)
            delta[y] -= 1
            delta[x] += 1
            cnt -= 1
            zero = z

        dfs(0)
        return res

    """
    方法二：二进制枚举
    我们可以使用一个长度为 m 的二进制数 mask 表示所有的请求，其中 mask 从低到高的第 i 位为 1 表示选择第 i 个请求，
    为 0 表示不选第 i 个请求。我们可以枚举[0,2^m−1] 范围内的所有 mask，对于每个 mask，依次枚举其每一位，判断是否为 1，
    并使用与方法一相同的数组 delta 以及变量 cnt 进行统计，在满足要求时更新答案。
    
    复杂度分析
    · 时间复杂度：O(2^m × n)，其中 m 是数组 requests 的长度，即请求的数量。从 m 个请求中任意选择请求的方案数为 2^m，
    对于每一种方案，我们需要 O(n) 的时间判断其是否满足要求。
    · 空间复杂度：O(n)。delta 需要 O(n) 的空间。

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        for mask in range(1 << len(requests)):
            cnt = mask.bit_count()
            if cnt <= ans:
                continue
            delta = [0] * n
            for i, (x, y) in enumerate(requests):
                if mask & (1 << i):
                    delta[x] += 1
                    delta[y] -= 1
            if all(x == 0 for x in delta):
                ans = cnt
        return ans
    """


if __name__ == "__main__":
    n = 3
    nums = [[0,0],[1,1],[0,0],[2,0],[2,2],[1,1],[2,1],[0,1],[0,1]]
    s = Solution()
    print(s.maximumRequests(n, nums))


