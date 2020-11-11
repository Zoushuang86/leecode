"""
88. 合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。



说明：

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。


示例：

输入：
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出：[1,2,2,3,5,6]


提示：

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
"""

"""
双指针向前比较法
复杂度分析
时间复杂度 : O(n + m)
空间复杂度 : O(1)
"""
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        # two get pointers for nums1 and nums2
        p1 = m - 1
        p2 = n - 1
        # set pointer for nums1
        p = m + n - 1

        # while there are still elements to compare
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        # add missing elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]


"""
双指针向后比较
执行用时：36 ms, 在所有 Python3 提交中击败了88.88%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了9.83%的用户
复杂度分析
时间复杂度 : O(n + m)O(n+m)。
空间复杂度 : O(m)O(m)。

class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        nums1_copy = nums1[:m]
        nums1[:] = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1_copy[i] < nums2[j]:
                nums1.append(nums1_copy[i])
                i += 1
            else:
                nums1.append(nums2[j])
                j += 1
        if i < m:
            nums1[i+j:] = nums1_copy[i:]
        if j < n:
            nums1[i+j:] = nums2[j:]
        print(nums1)
"""

"""
合并排序法
执行用时：44 ms, 在所有 Python3 提交中击败了46.00%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了9.13%的用户
复杂度分析
时间复杂度 : O((n + m)\log(n + m))O((n+m)log(n+m))。
空间复杂度 : O(1)O(1)。
时间复杂度较差，为O((n+m)log(n+m))。这是由于这种方法没有利用两个数组本身已经有序这一点。
class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()
        print(nums1)
"""

if __name__ == "__main__":
    nums1 = []
    nums2 = []
    Solution().merge(nums1, len(nums1)-len(nums2), nums2, len(nums2))
