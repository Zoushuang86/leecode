"""
面试题 17.14. 最小K个数
设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。

示例：

输入： arr = [1,3,5,7,2,4,6,8], k = 4
输出： [1,2,3,4]
提示：

0 <= len(arr) <= 100000
0 <= k <= min(100000, len(arr))
"""
from queue import PriorityQueue
class Solution:
    def smallestK(self, arr, k):
        if len(arr) == 0 or k == 0:
            return []

        pq = PriorityQueue(k)
        for e in arr:
            if pq.qsize() < k:
                pq.put(-e)
            else:
                temp = pq.get()
                if -e > temp:
                    pq.put(-e)
                else:
                    pq.put(temp)

        res = []
        while not pq.empty():
            res.append(-pq.get())
        return res


if __name__ == "__main__":
    nums = [1,3,5,7,2,4,6,8]
    k = 5
    s = Solution()
    print(s.smallestK(nums, k))
