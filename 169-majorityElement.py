"""
169. 多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。



示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
"""

"""
执行用时：56 ms, 在所有 Python3 提交中击败了49.88%的用户
内存消耗：14.9 MB, 在所有 Python3 提交中击败了27.84%的用户
"""

class Solution:
    def majorityElement(self, nums: list) -> int:
        nums = sorted(nums)
        target = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == target:
                count += 1
            else:
                if count > len(nums) // 2:
                    return target
                else:
                    target = nums[i]
                    count = 1
        if count > len(nums) // 2:
            return target


"""
如果将数组 nums 中的所有元素按照单调递增或单调递减的顺序排序，那么下标为⌊2/n⌋ 的元素（下标从 0 开始）一定是众数。

执行用时：48 ms, 在所有 Python3 提交中击败了78.92%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了10.40%的用户
"""
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]

"""
哈希表统计

执行用时：44 ms, 在所有 Python3 提交中击败了89.58%的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了15.04%的用户
"""
import collections
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

if __name__ == "__main__":
    nums1 = [3,2,3]
    print(Solution().majorityElement(nums1))
