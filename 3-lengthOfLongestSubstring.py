"""
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

"""
执行用时：68 ms, 在所有 Python3 提交中击败了83.89%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了10.76%的用户

class Solution:
    
    执行用时：124 ms, 在所有 Python3 提交中击败了17.77%的用户
    内存消耗：14.9 MB, 在所有 Python3 提交中击败了88.75%的用户
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = list(s)
        freq = [0 for i in range(256)]  # 所有字符的ASCII码频率
        left, right = 0, -1     # 滑动窗口s[left, right]
        result = 0
        while left < len(arr):
            if (right+1 < len(arr)) and (freq[ord(arr[right+1])] == 0):
                right += 1
                freq[ord(arr[right])] += 1
            else:
                freq[ord(arr[left])] -= 1
                left += 1
            result = max(result, right-left+1)
        return result
"""

# 动态规划+hash表
"""
哈希表 dic 统计： 指针 j 遍历字符 s ，哈希表统计字符 s[j] 最后一次出现的索引 。
更新左指针 i ： 根据上轮左指针 i 和 dic[s[j]] ，每轮更新左边界 i ，保证区间 [i+1,j] 内无重复字符且最大。
i=max(dic[s[j]],i)

更新结果 res ： 取上轮 res 和本轮双指针区间 [i+1,j] 的宽度（即 j−i ）中的最大值。
res=max(res,j−i)

复杂度分析：
时间复杂度 O(N) ： 其中 NN 为字符串长度，动态规划需遍历计算 dp 列表。
空间复杂度 O(1) ： 字符的 ASCII 码范围为 0 ~ 127 ，哈希表 dic 最多使用 O(128)=O(1) 大小的额外空间。
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = dict()
        res = 0
        i = -1
        for j in range(len(s)):
            if s[j] in map:
                i = max(map[s[j]], i)
            map[s[j]] = j
            res = max(res, j-i)
        return res



if __name__ == "__main__":
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))