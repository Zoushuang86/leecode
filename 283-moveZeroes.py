"""
283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""
"""
执行用时：52 ms, 在所有 Python3 提交中击败了30.54%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.51%的用户
class Solution:
        # Do not return anything, modify nums in-place instead.
        def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for index in range(len(nums)):
            if nums[index] == 0:
                count += 1
                nums[count:index+1] = nums[count-1:index]
                nums[count-1] = 0
        nums[:] = nums[count:] + [0]*count
"""
"""
方法二：栈弹出0，追加0
当前坐标根据0个数动态调整
执行用时：40 ms, 在所有 Python3 提交中击败了77.26%的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了5.51%的用户
"""
class Solution:
    def moveZeroes(self, nums):
        # Do not return anything, modify nums in-place instead.
        count = 0
        for index in range(len(nums)):
            idx = index - count
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
                count += 1
        return nums


if __name__ == "__main__":
    A = [0,1,0,3,12]
    s = Solution()
    print(s.moveZeroes(A))

