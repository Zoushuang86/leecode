"""
剑指 Offer 26. 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：

0 <= 节点个数 <= 10000
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 定义：判断以A为根节点的子树是否包含B子树
    def recur(self, A: TreeNode, B: TreeNode) -> bool:
        # B被遍历完成，说明包含
        if not B:
            return True
        # A和B不匹配
        if not A or A.val != B.val:
            return False
        return self.recur(A.left, B.left) and self.recur(A.right, B.right)

    # 定义：先序遍历A的所有节点
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        return bool(A and B) and (self.recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
