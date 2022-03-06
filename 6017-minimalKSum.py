class Solution:
    def minimalKSum(self, nums: list, k: int) -> int:
        # 增加两个哨兵，当时只想到一个0
        nums.append(0)
        nums.append(10**10)
        nums = sorted(list(set(nums)))
        res = 0
        i = 0
        # 注意i边界条件，WA了好几次T^T
        while k > 0 and i < len(nums) - 1:
            n = nums[i+1] - nums[i] - 1
            if n >= 1:
                if k >= n:
                    res += ((nums[i] + 1) + (nums[i+1] - 1)) * n // 2
                    k -= n
                else:
                    res += ((nums[i] + 1) + (nums[i] + k)) * k // 2
                    k = 0
            i += 1
        return res