"""
1588. 所有奇数长度子数组的和
给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。

子数组 定义为原数组中的一个连续子序列。

请你返回 arr 中 所有奇数长度子数组的和 。



示例 1：

输入：arr = [1,4,2,5,3]
输出：58
解释：所有奇数长度子数组和它们的和为：
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
示例 2：

输入：arr = [1,2]
输出：3
解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。
示例 3：

输入：arr = [10,11,12]
输出：66


提示：

1 <= arr.length <= 100
1 <= arr[i] <= 1000
"""

"""
方法一：直接计算

执行用时：68 ms, 在所有 Python3 提交中击败了56.06%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了5.00%的用户

时间复杂度：O(n^2)
空间复杂度：O(1)

class Solution:
    def sumOddLengthSubarrays(self, arr):
        res = 0
        for length in range(1, len(arr)+1):
            if length % 2 == 1:
                for i in range(len(arr)-length+1):
                    res += sum(arr[i: i+length])
        return res
"""

"""
方法二：计算每个元素出现在奇数长度子序列的次数

一个元素arr[i]出现在奇数长度子序列，除去本身，左右两边还有偶数个其他元素
存在两种情况：
1. 偶数+偶数=偶数
2. 奇数+奇数=偶数

对于情况一：只需求得左侧偶数长度有多少种 left_even，和右侧偶数长度有多少种 right_even；
注意，0也是一种可能
对于情况二：只需求得左侧奇数长度有多少种 left_odd，和右侧奇数长度有多少种 right_odd；

因此，arr[i]出现在奇数长度子序列的次数为 left_odd*right_odd + left_even*right_even


执行用时：52 ms, 在所有 Python3 提交中击败了86.27%的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了5.00%的用户

时间复杂度：O(n)
空间复杂度：O(1)

"""
class Solution:
    def sumOddLengthSubarrays(self, arr):
        res = 0
        for index, item in enumerate(arr):
            left, right = index + 1, len(arr) - index   # +1考虑长度为0的情况
            left_even = (left + 1) // 2
            right_even = (right + 1) // 2
            left_odd = left // 2
            right_odd = right // 2
            res += (left_odd*right_odd + left_even*right_even) * item
        return res


if __name__ == "__main__":
    A = [1,2]
    s = Solution()
    print(s.sumOddLengthSubarrays(A))
