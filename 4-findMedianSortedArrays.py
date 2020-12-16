"""
4. 寻找两个正序数组的中位数
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？



示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：

输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：

输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：

输入：nums1 = [2], nums2 = []
输出：2.00000


提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

"""
执行用时：64 ms, 在所有 Python3 提交中击败了31.28%的用户
内存消耗：13.7 MB, 在所有 Python3 提交中击败了7.42%的用户
"""
class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        if len(nums1) % 2 == 1:
            return nums1[len(nums1) // 2]
        else:
            return (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2


"""
根据中位数的定义，当 m+nm+n 是奇数时，中位数是两个有序数组中的第 (m+n)/2个元素，
当 m+nm+n 是偶数时，中位数是两个有序数组中的第 (m+n)/2 个元素和第 (m+n)/2+1 个元素的平均值。
因此，这道题可以转化成寻找两个有序数组中的第 k 小的数，其中 kk 为 (m+n)/2 或 (m+n)/2+1。
"""


if __name__ == "__main__":
    nums1 = [1, 2]
    nums2 = [3]
    print(Solution().findMedianSortedArrays(nums1, nums2))