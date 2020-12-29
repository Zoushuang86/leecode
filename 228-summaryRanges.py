"""
228. 汇总区间
给定一个无重复元素的有序整数数组 nums 。

返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。
也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，
并且不存在属于某个范围但不属于 nums 的数字 x 。

列表中的每个区间范围 [a,b] 应该按如下格式输出：

"a->b" ，如果 a != b
"a" ，如果 a == b


示例 1：

输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
示例 2：

输入：nums = [0,2,3,4,6,8,9]
输出：["0","2->4","6","8->9"]
解释：区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
示例 3：

输入：nums = []
输出：[]
示例 4：

输入：nums = [-1]
输出：["-1"]
示例 5：

输入：nums = [0]
输出：["0"]


提示：

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
nums 中的所有值都 互不相同
"""

"""
执行用时：36 ms, 在所有 Python3 提交中击败了75.32%的用户
内存消耗：14.8 MB, 在所有 Python3 提交中击败了5.39%的用户
"""

class Solution:
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        else:
            results = []
            start = nums[0]
            end = nums[0] + 1
            for e in nums[1:]:
                if e == end:
                    end += 1
                else:
                    if end - 1 == start:
                        results.append(str(start))
                    else:
                        results.append(str(start)+"->"+str(end-1))
                    start = e
                    end = e + 1
            if end - 1 == start:
                results.append(str(start))
            else:
                results.append(str(start) + "->" + str(end - 1))
            return results


if __name__ == "__main__":
    A = [1]
    s = Solution()
    print(s.summaryRanges(A))
