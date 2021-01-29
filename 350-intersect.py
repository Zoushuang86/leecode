"""
350. 两个数组的交集 II
给定两个数组，编写一个函数来计算它们的交集。



示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]


说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
通过次数167,35
"""
"""
执行用时：72 ms, 在所有 Python3 提交中击败了28.45%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了7.17%的用户

class Solution:
    def intersect(self, nums1, nums2):
        res = []
        for e in nums1:
            if e in nums2:
                res.append(e)
                nums2.remove(e)
        return res
"""
"""
hash表
执行用时：52 ms, 在所有 Python3 提交中击败了89.63%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了5.15%的用户
"""
class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        import collections
        m = collections.Counter()
        for num in nums1:
            m[num] += 1

        intersection = list()
        for num in nums2:
            while m:
                if m.get(num, 0) > 0:
                    intersection.append(num)
                    m[num] -= 1
                    if m[num] == 0:
                        m.pop(num)

        return intersection

if __name__ == "__main__":
    s = [1,2,2,1]
    t = [2, 2]
    A = Solution()
    print(A.intersect(s, t))