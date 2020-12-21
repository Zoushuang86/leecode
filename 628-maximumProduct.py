"""
628. 三个数的最大乘积
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
注意:

给定的整型数组长度范围是[3,10^4]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。
"""

"""
方法一：基于排序

我们将数组进行升序排序，如果数组中所有的元素都是非负数，那么答案即为最后三个元素的乘积。
如果数组中出现了负数，那么我们还需要考虑乘积中包含负数的情况，显然选择最小的两个负数和最大的一个正数是最优的，
即为前两个元素与最后一个元素的乘积。
上述两个结果中的较大值就是答案。注意我们可以不用判断数组中到底有没有正数，0 或者负数，
因为上述两个结果实际上已经包含了所有情况，最大值一定在其中。

复杂度分析
时间复杂度：O(NlogN)，其中 N 是数组的长度。
空间复杂度：O(logN)，为排序使用的空间。

执行用时：84 ms, 在所有 Python3 提交中击败了75.40%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了5.22%的用户

class Solution:
    def maximumProduct(self, nums):
        nums = sorted(nums)
        return max(nums[0]*nums[1]*nums[-1], nums[-3]*nums[-2]*nums[-1])
"""

"""
方法二：线性扫描
直接线性扫描最大的三个元素和最小的两个元素即可

复杂度分析
时间复杂度：O(N)，其中 N 是数组的长度。
空间复杂度：O(1)。

执行用时：68 ms, 在所有 Python3 提交中击败了95.09%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了5.22%的用户
"""

class Solution:
    def maximumProduct(self, nums):
        max1, max2, max3 = -1001, -1001, -1001
        min1, min2 = 1001, 1001
        for element in nums:
            if element < min1:
                min2 = min1
                min1 = element
            elif element < min2:
                min2 = element
            if element > max1:
                max3 = max2
                max2 = max1
                max1 = element
            elif element > max2:
                max3 = max2
                max2 = element
            elif element > max3:
                max3 = element
        return max(min1*min2*max1, max1*max2*max3)


if __name__ == "__main__":
    A = [-10, 0, 1, -9, -3]
    s = Solution()
    print(s.maximumProduct(A))
