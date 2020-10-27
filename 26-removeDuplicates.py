"""
26. 删除排序数组中的重复项
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。



示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。


说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""


"""
执行用时：1024 ms, 在所有 Python3 提交中击败了8.16%的用户
内存消耗：14.5 MB, 在所有 Python3 提交中击败了15.00%的用户
"""
"""
class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 1
        j = 0
        while j < len(nums)-1:
            if nums[i] == nums[i-1]:
                nums[i: len(nums)-1] = nums[i+1: len(nums)]
            else:
                i += 1
            j += 1
            print(nums)
        return i, nums
"""
"""
执行用时：32 ms, 在所有 Python3 提交中击败了99.66%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了5.11%的用户
"""
class Solution:
    def removeDuplicates(self, nums) -> int:
        # 切片赋值是真正修改内容
        nums[:] = list(sorted(set(nums)))
        return len(nums), nums



if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    s = Solution()
    r, l = s.removeDuplicates(nums)
    print(r, l)

