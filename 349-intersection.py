"""
349. 两个数组的交集
给定两个数组，编写一个函数来计算它们的交集。



示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]


说明：

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
"""
class Solution:
    """
    执行用时：40 ms, 在所有 Python3 提交中击败了40.82%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了26.35%的用户

    def intersection(self, nums1, nums2):
        return list(set(nums1).intersection(set(nums2)))
    """
    """
    执行用时：28 ms, 在所有 Python3 提交中击败了93.28%的用户
    内存消耗：15.1 MB, 在所有 Python3 提交中击败了48.56%的用户
    """
    def intersection(self, nums1, nums2):
        record = set(nums1)
        resultSet = []
        for e in nums2:
            if (e in record) and (e not in resultSet):
                resultSet.append(e)
        return resultSet


if __name__ == "__main__":
    A = [4,9,5]
    p = [9,4,9,8,4]
    s = Solution()
    print(s.intersection(A, p))
