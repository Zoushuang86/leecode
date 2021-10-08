"""
454. 四数相加 II
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
# 时间复杂度：O(n^2)
# 空间复杂度：O(n^2)
class Solution:
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # 存放C+D和sum，以及出现次数count：{sum:count}
        record = {}
        for i in nums3:
            for j in nums4:
                if record.get(i + j) == None:
                    record[i + j] = 1
                else:
                    record[i + j] += 1

        res = 0
        for i in nums1:
            for j in nums2:
                if record.get(0 - i - j) != None:
                    res += record[0 - i - j]
        return res


if __name__ == "__main__":
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(Solution().fourSumCount(A, B, C, D))
