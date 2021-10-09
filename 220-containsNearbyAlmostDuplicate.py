"""
220. 存在重复元素 III
给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。

如果存在则返回 true，不存在返回 false。



示例 1：

输入：nums = [1,2,3,1], k = 3, t = 0
输出：true
示例 2：

输入：nums = [1,0,1,1], k = 1, t = 2
输出：true
示例 3：

输入：nums = [1,5,9,1,5,9], k = 2, t = 3
输出：false


提示：

0 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 104
0 <= t <= 231 - 1
"""
"""
普通滑动窗口:超时

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        kSet = set()
        for i in range(len(nums)):
            for j in kSet:
                if abs(nums[i]-j) <= t:
                    return True
            kSet.add(nums[i])
            if len(kSet) > k:
                kSet.remove(nums[i - k])
        return False
"""

from sortedcontainers import SortedList
class Solution:
    # 使用二分查找树进行存储
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        window = SortedList()
        for i in range(len(nums)):
            # 假设这个值是 x，就是 nums[i] - t <= x。我们又要求了 x <= nums[i] + t，所以：
            # nums[i] - t <= x <= nums[i] + t
            j = window.bisect_left(nums[i]-t)
            if j != len(window) and window[j] <= nums[i]+t:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.discard(nums[i - k])
        return False


if __name__ == "__main__":
    points = [2147483647, -1, 2147483647]
    k = 1
    t = 2147483647
    print(Solution().containsNearbyAlmostDuplicate(points,k,t))
