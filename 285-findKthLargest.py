"""
215. 数组中的第K个最大元素
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。



示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4


提示：

1 <= k <= nums.length <= 104
-104 <= nums[i] <= 104
"""

"""
方法一：快速排序
① 原始版本
执行用时：452 ms, 在所有 Python3 提交中击败了35.04%的用户
内存消耗：19.4 MB, 在所有 Python3 提交中击败了22.06%的用户
② 随机初始化v
执行用时：40 ms, 在所有 Python3 提交中击败了71.72%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了30.82%的用户
③ 当数组小于15使用插入排序
执行用时：40 ms, 在所有 Python3 提交中击败了71.72%的用户
内存消耗：15.8 MB, 在所有 Python3 提交中击败了27.69%的用户
"""
import random

class Solution:
    def __insertion_sort(self, arr, left: int, right: int):
        for i in range(left + 1, right + 1):
            # 寻找元素arr[i]合适的插入位置
            e = arr[i]
            for j in range(i, left - 1, -1):
                if e < arr[j - 1]:
                    arr[j] = arr[j - 1]
                else:
                    break
            arr[j] = e

    def __partition(self, nums, left, right):
        random_index = random.randint(left, right)
        nums[left], nums[random_index] = nums[random_index], nums[left]
        v = nums[left]
        # nums[left+1,j]<v<[j+1,i)
        # 初始化时，两个区间都为空
        j = left
        for i in range(left+1, right+1):
            if nums[i] < v:
                nums[j+1], nums[i] = nums[i], nums[j+1]
                j += 1
        nums[left], nums[j] = nums[j], nums[left]
        return j

    def __quick_sort(self, nums, left, right, index):
        # if left >= right:
        #     return
        if right - left <= 15:
            self.__insertion_sort(nums, left, right)
            return
        p = self.__partition(nums, left, right)
        if p == index:
            return
        elif p > index:
            self.__quick_sort(nums, left, p-1, index)
        else:
            self.__quick_sort(nums, p+1, right, index)

    def findKthLargest(self, nums, k):
        self.__quick_sort(nums, 0, len(nums)-1, len(nums)-k)
        return nums[len(nums)-k]



if __name__ == "__main__":
    A = [3,2,3,1,2,4,5,5,6]
    k = 4
    s = Solution()
    print(s.findKthLargest(A, k))
