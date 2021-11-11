"""
131. 分割回文串
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。



示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]


提示：

1 <= s.length <= 16
s 仅由小写英文字母组成
"""
class Solution:
    def partition(self, s: str) -> list:
        res = []
        ans = []

        def isPalindrome(i, j):
            string = s[i:j+1]
            return string == string[::-1]

        def dfs(start: int):
            # print("start: {}".format(start))
            # 已经遍历完成
            if start == len(s):
                res.append(ans[:])
                # print("get a results: {}\n".format(str(ans[:])))
                return

            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    ans.append(s[start:end+1])
                    # print("append a string s[{}:{}] = {}:".format(start, end, s[start:end+1]))
                    dfs(end+1)
                    ans.pop()

        dfs(0)
        return res


if __name__ == "__main__":
    A = "aab"
    s = Solution()
    print(s.partition(A))
