"""
108. 将有序数组转换为二叉搜索树
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。



示例 1：


输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

示例 2：


输入：nums = [1,3]
输出：[3,1]
解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。


提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 按 严格递增 顺序排列
"""
from binary_tree import *
class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        if len(nums) == 0:
            return None
        return self.createBST(nums, 0, len(nums)-1)

    # nums[left, right]区间建立BST，返回根节点
    def createBST(self, nums, left, right) -> TreeNode:
        if left > right:
            return
        mid = (right - left) // 2 + left
        node = TreeNode(nums[mid])
        node.left = self.createBST(nums, left, mid - 1)
        node.right = self.createBST(nums, mid + 1, right)
        return node


if __name__ == "__main__":
    s = Solution()
    arr = [1,2,3,4,5]
    root = s.sortedArrayToBST(arr)
    inorder(root)
