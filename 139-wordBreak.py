"""
139. 单词拆分
给你一个字符串 s 和一个字符串列表 wordDict 作为字典，判定 s 是否可以由空格拆分为一个或多个在字典中出现的单词。

说明：拆分时可以重复使用字典中的单词。



示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false


提示：

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s 和 wordDict[i] 仅有小写英文字母组成
wordDict 中的所有字符串 互不相同
"""
"""
dp[i] 表示字符串 s 前 i 个字符组成的字符串 s[0..i−1] 是否能被空格拆分成若干个字典中出现的单词。

转移方程：dp[i]=dp[j] && check(s[j..i−1])
其中 check(s[j..i−1]) 表示子串 s[j..i−1] 是否出现在字典中。
对于边界条件，我们定义 dp[0]=true 表示空串且合法。
"""
class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        wordHash = dict()
        for word in wordDict:
            wordHash[word] = 1
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True
        for i in range(n+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordHash:
                    dp[i] = True
                    break
        return dp[n]


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    solution = Solution()
    print(solution.wordBreak(s, wordDict))

