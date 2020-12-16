"""
面试题 17.10. 主要元素
数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。

示例 1：

输入：[1,2,5,9,5,9,5,5,5]
输出：5


示例 2：

输入：[3,2]
输出：-1


示例 3：

输入：[2,2,1,1,1,2,2]
输出：2


说明：
你有办法在时间复杂度为 O(N)，空间复杂度为 O(1) 内完成吗？
"""


"""
执行用时：36 ms, 在所有 Python3 提交中击败了98.97%的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了5.08%的用户
"""
class Solution:
    def majorityElement(self, nums):
        for item in set(nums):
            if nums.count(item) > (len(nums) // 2):
                return item
        return -1


if __name__ == "__main__":
    A = [1,2,5,9,5,9,5,5,5]
    s = Solution()
    print(s.majorityElement(A))
