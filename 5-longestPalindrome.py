"""
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""

"""
执行超时
class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        for length in range(slen, 0, -1):
            for i in range(slen-length+1):
                if s[i:i+length] == s[i+length-slen-1:i-slen-1:-1]:
                    return s[i:i+length]
"""

"""
动态规划：子序列为回文子串，则去掉头尾剩余部分依旧是回文子串
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        dp = [[False]*length for _ in range(length)]
        ans = ""
        # 枚举子串的长度l+1
        for l in range(length):
            # 枚举子串起始位置i
            for i in range(length):
                j = i + l
                if j > length:
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] and s[i] == s[j])
                if dp[i][j] and l+1 > len(ans):
                    ans = s[i][j+1]
        return ans


if __name__ == "__main__":
    A = "cbbd"
    s = Solution()
    print(s.longestPalindrome(A))
