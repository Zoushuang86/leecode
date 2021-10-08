"""
16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。



示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。


提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
"""

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        best = 10**7

        def update(cur):
            nonlocal best
            if abs(cur -target) < abs(best-target):
                best = cur

        for a in range(len(nums)):
            # 保证和上一次枚举的元素不相等
            if a > 0 and nums[a] == nums[a-1]:
                continue
            b = a + 1
            c = len(nums) - 1
            while b < c:
                s = nums[a] + nums[b] + nums[c]
                if s == target:
                    return target
                update(s)
                if s > target:
                    # 如果和大于 target，移动 c 对应的指针
                    while b < c and nums[c-1] == nums[c]:
                        c -= 1
                    c -= 1
                else:
                    # 如果和小于 target，移动 b 对应的指针
                    while b < c and nums[b] == nums[b+1]:
                        b += 1
                    b += 1

        return best


if __name__ == "__main__":
    nums1 = [-1,2,1,-4]
    target = 1
    print(Solution().threeSumClosest(nums1, target))