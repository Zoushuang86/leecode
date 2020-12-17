"""
977. 有序数组的平方
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。



示例 1：

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
示例 2：

输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]


提示：

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A 已按非递减顺序排序。
"""

"""
方法一：直接排序
执行用时：52 ms, 在所有 Python3 提交中击败了99.95%的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了5.17%的用户

复杂度分析
时间复杂度：O(nlogn)，其中 n 是数组 A 的长度。
空间复杂度：O(logn)。除了存储答案的数组以外，我们需要 O(logn) 的栈空间进行排序。



class Solution:
    def sortedSquares(self, nums):
        return sorted([x*x for x in nums])
"""

"""
方法二：双指针
利用「数组 AA 已经按照升序排序」条件，找到数组 A 中负数与非负数的分界线negative，
将数组 A 中的数平方后，得到了两个已经有序的子数组，因此就可以使用归并的方法进行排序了。

执行用时：92 ms, 在所有 Python3 提交中击败了98.84%的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了5.17%的用户

复杂度分析
时间复杂度：O(n)，其中 n 是数组 A 的长度。
空间复杂度：O(1)。

class Solution:
    def sortedSquares(self, nums):
        length = len(nums)
        negative = -1
        for i, num in enumerate(nums):
            if num < 0:
                negative = i
            else:
                break

        ans = list()
        i, j = negative, negative+1
        while i >= 0 or j < length:
            if i < 0:
                ans.append(nums[j]*nums[j])
                j += 1
            elif j >= length:
                ans.append(nums[i]*nums[i])
                i -= 1
            elif nums[i]*nums[i] < nums[j]*nums[j]:
                ans.append(nums[i]*nums[i])
                i -= 1
            else:
                ans.append(nums[j]*nums[j])
                j += 1
        return ans
"""

"""
方法三：双指针
我们可以使用两个指针分别指向位置 0 和 n-1，每次比较两个指针对应的数，
选择较大的那个逆序放入答案并移动指针。这种方法无需处理某一指针移动至边界的情况，

执行用时：256 ms, 在所有 Python3 提交中击败了56.86%的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了5.17%的用户

复杂度分析
时间复杂度：O(n)，其中 n 是数组 A 的长度。
空间复杂度：O(1)。
"""

class Solution:
    def sortedSquares(self, nums):
        ans = list()
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i]*nums[i] < nums[j]*nums[j]:
                ans.insert(0, nums[j]*nums[j])
                j -= 1
            else:
                ans.insert(0, nums[i] * nums[i])
                i += 1
        return ans


if __name__ == "__main__":
    A = [-4,-1,0,3,10]
    s = Solution()
    print(s.sortedSquares(A))
