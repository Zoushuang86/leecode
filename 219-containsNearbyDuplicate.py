"""
219. 存在重复元素 II
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，
并且 i 和 j 的差的 绝对值 至多为 k。

示例 1:

输入: nums = [1,2,3,1], k = 3
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1
输出: true
示例 3:

输入: nums = [1,2,3,1,2,3], k = 2
输出: false
"""
"""
执行用时：9648 ms, 在所有 Python3 提交中击败了5.05%的用户
内存消耗：17.6 MB, 在所有 Python3 提交中击败了97.56%的用户

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        for index in range(len(nums)):
            try:
                if nums.index(nums[index], max(index-k, 0), min(index+k, len(nums))) != index:
                    return True
            except:
                pass
        return False
"""
"""
维护一个长为k的Hash集合
执行用时：44 ms, 在所有 Python3 提交中击败了82.38%的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了82.46%的用户
"""
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        kSet = set()
        for i in range(len(nums)):
            if kSet.__contains__(nums[i]):
                return True
            kSet.add(nums[i])
            if len(kSet) > k:
                kSet.remove(nums[i-k])
        return False


if __name__ == "__main__":
    A = [1,2,3,1,2,3]
    k = 2
    s = Solution()
    print(s.containsNearbyDuplicate(A, k))

