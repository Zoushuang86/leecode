"""
75. 颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]
示例 3：

输入：nums = [0]
输出：[0]
示例 4：

输入：nums = [1]
输出：[1]


提示：

n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2


进阶：

你可以不使用代码库中的排序函数来解决这道题吗？
你能想出一个仅使用常数空间的一趟扫描算法吗？
"""

class Solution:
    """
    # O(n) O(1)
    def sortColors(self, nums):
        # Do not return anything, modify nums in-place instead.
        count = [0, 0, 0]   # 存放0,1,2三个元素的频率
        for i in range(len(nums)):
            assert 0 <= nums[i] <= 2
            count[nums[i]] += 1

        index = 0
        for i in range(count[0]):
            nums[index] = 0
            index += 1
        for i in range(count[1]):
            nums[index] = 1
            index += 1
        for i in range(count[2]):
            nums[index] = 2
            index += 1
    """
    """
    执行用时：36 ms, 在所有 Python3 提交中击败了44.01%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了76.85%的用户
    """
    def sortColors(self, nums):
        # Do not return anything, modify nums in-place instead.
        zero = -1           # nums[0,zero] == 0
        two = len(nums)     # nums[two, n-1] == 2
        i = 0
        while i < two:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                two -= 1
                nums[two], nums[i] = nums[i], nums[two]
            else:
                assert nums[i] == 0
                zero += 1
                nums[zero], nums[i] = nums[i], nums[zero]
                i += 1
        return nums


if __name__ == "__main__":
    A = [2,0,2,1,1,0]
    s = Solution()
    print(s.sortColors(A))

