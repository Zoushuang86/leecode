"""
1189. “气球” 的最大数量
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。

字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。



示例 1：



输入：text = "nlaebolko"
输出：1
示例 2：



输入：text = "loonbalxballpoon"
输出：2
示例 3：

输入：text = "leetcode"
输出：0


提示：

1 <= text.length <= 10^4
text 全部由小写英文字母组成
"""
"""
执行用时：28 ms, 在所有 Python3 提交中击败了96.40%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了19.52%的用户
"""
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        sub = {'l': 2, 'o': 2, 'b': 1, 'a': 1, 'n': 1}
        count = {'l': 0, 'o': 0, 'b': 0, 'a': 0, 'n': 0}
        for i in text:
            if i in ['l', 'o', 'b', 'a', 'n']:
                count[i] += 1
        res = len(text)
        for key in count:
                res = min(res, count[key] // sub[key])
        return res




if __name__ == "__main__":
    text = "loonbalxballpoon"
    s = Solution()
    print(s.maxNumberOfBalloons(text))
