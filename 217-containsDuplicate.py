"""
217. 存在重复元素
给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。



示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
"""
"""
执行用时：52 ms, 在所有 Python3 提交中击败了30.58%的用户
内存消耗：20.2 MB, 在所有 Python3 提交中击败了20.18%的用户

"""
class Solution:
    def containsDuplicate(self, nums):
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

"""
执行用时：44 ms, 在所有 Python3 提交中击败了71.98%的用户
内存消耗：20.2 MB, 在所有 Python3 提交中击败了21.08%的用户
"""
class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    A = [1,2]
    s = Solution()
    print(s.containsDuplicate(A))
