"""
337. 打家劫舍 III
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.
示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.
"""
from binary_tree import *
from collections import defaultdict


class Solution:
    # f为选中node，g为不选中node
    f, g = defaultdict(int), defaultdict(int)

    def __dfs(self, node: TreeNode):
        if not node:
            return

        self.__dfs(node.left)
        self.__dfs(node.right)
        self.f[node] = node.val + self.g[node.left] + self.g[node.right]
        self.g[node] = max(self.f[node.left], self.g[node.left]) +\
                       max(self.f[node.right], self.g[node.right])

    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.__dfs(root)
        return max(self.f[root], self.g[root])


if __name__ == "__main__":
    s = Solution()
    arr = [2,1,3,None,4]
    root = creatTree(arr)
    print(s.rob(root))

