"""
438. 找到字符串中所有字母异位词
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指字母相同，但排列不同的字符串。



示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。


提示:

1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母
"""

class Solution:
    """
    滑动窗口+双指针
    执行用时：84 ms, 在所有 Python3 提交中击败了66.22%的用户
    内存消耗：15.4 MB, 在所有 Python3 提交中击败了30.26%的用户

    定义滑动窗口的左右两个指针left，right
    right一步一步向右走遍历s字符串
    right当前遍历到的字符加入s_cnt后不满足p_cnt的字符数量要求，将滑动窗口左侧字符不断弹出，也就是left不断右移，直到符合要求为止。
    当滑动窗口的长度等于p的长度时，这时的s子字符串就是p的异位词。
    其中，left和right表示滑动窗口在字符串s中的索引，cur_left和cur_right表示字符串s中索引为left和right的字符在数组中的索引
    """
    def findAnagrams(self, s: str, p: str) -> list:
        n, m, res = len(s), len(p), []
        if n < m: return res
        p_cnt = [0] * 26
        s_cnt = [0] * 26

        for i in range(m):
            p_cnt[ord(p[i]) - ord('a')] += 1

        left = 0
        for right in range(n):
            cur_right = ord(s[right]) - ord('a')
            s_cnt[cur_right] += 1
            while s_cnt[cur_right] > p_cnt[cur_right]:
                cur_left = ord(s[left]) - ord('a')
                s_cnt[cur_left] -= 1
                left += 1
            if right - left + 1 == m:
                res.append(left)
        return res


if __name__ == "__main__":
    A = "cbaebabacd"
    p = "abc"
    s = Solution()
    print(s.findAnagrams(A, p))
