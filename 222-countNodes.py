"""
222. 完全二叉树的节点个数
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。



示例 1：


输入：root = [1,2,3,4,5,6]
输出：6
示例 2：

输入：root = []
输出：0
示例 3：

输入：root = [1]
输出：1


提示：

树中节点的数目范围是[0, 5 * 104]
0 <= Node.val <= 5 * 104
题目数据保证输入的树是 完全二叉树


进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？
"""
from binary_tree import *
"""
递归方法：O(n)

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        return self.countNodes(root.right) + self.countNodes(root.left) + 1
"""

"""
二分查找法+位运算：O(logn*logn)
"""
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 找到最大深度，根据完全二叉树性质，遍历左子树的左孩子即可
        level = 0
        node = root
        while node.left:
            level += 1
            node = node.left

        # 确定节点数量最小和最大范围
        low = 1 << level                # 最小为pow(2, level)
        high = (1 << (level+1)) - 1     # 最大为pow(2, level+1)-1
        # 不断二分搜索查找是否存在该范围的中间节点，并找到最大值
        while low < high:
            mid = (high - low + 1) // 2 + low
            if self.exits(root, level, mid):
                low = mid
            else:
                high = mid - 1
        return low

    def exits(self, root, level, path):
        bits = 1 << (level - 1) # 从最高位开始遍历
        node = root
        while (node != None) and (bits > 0):
            # 位与，即按照高位依次从根节点遍历，0为左子树，1为右子树
            if not(bits & path):
                node = node.left
            else:
                node = node.right
            bits >>= 1  # 下一个层路径

        return node != None


if __name__ == "__main__":
    s = Solution()
    arr = [1,2,3,4,5,6,7,8,9]
    bt = BT(arr)
    print(s.countNodes(bt.root))
