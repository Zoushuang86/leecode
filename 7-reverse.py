"""
执行用时：44 ms, 在所有 Python3 提交中击败了68.61%的用户
内存消耗：13.4 MB, 在所有 Python3 提交中击败了11.03%的用户
"""
class Solution:
    def twoSum(self, x=321):
        if '-' in str(x):
            r = int("-" + str(x)[:0:-1])
        else:
            r = int(str(x)[::-1])
        if r > 2 ** 31 - 1 or r < -(2 ** 31):
            return 0
        else:
            return r


if __name__ == "__main__":
    x = -321
    s = Solution()
    print(s.twoSum(x))
