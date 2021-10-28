"""
347. 前 K 个高频元素
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。



示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]


提示：

1 <= nums.length <= 105
k 的取值范围是 [1, 数组中不相同的元素的个数]
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的


进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。
"""
import collections
from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums, k: int):
        # 统计每个元素出现的频率
        freq = collections.defaultdict(int)
        for e in nums:
            freq[e] += 1

        # 扫描freq，维护当前出现频率最高的k个元素
        # (freq, element)
        pq = PriorityQueue(k)
        for key, value in freq.items():
            if pq.qsize() == k:
                temp = pq.get()
                if value > temp[0]:
                    pq.put([value, key])
                else:
                    pq.put(temp)
            else:
                pq.put([value, key])

        res = []
        while not pq.empty():
            res.append(pq.get()[1])
        return res


if __name__ == "__main__":
    nums = [1,1,1,2,2,3,7,7,7,7,8,8,8,8,8]
    k = 2
    s = Solution()
    print(s.topKFrequent(nums, k))

