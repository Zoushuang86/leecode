"""
1405. 最长快乐字符串
如果字符串中不含有任何 'aaa'，'bbb' 或 'ccc' 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

给你三个整数 a，b ，c，请你返回 任意一个 满足下列全部条件的字符串 s：

s 是一个尽可能长的快乐字符串。
s 中 最多 有a 个字母 'a'、b 个字母 'b'、c 个字母 'c' 。
s 中只含有 'a'、'b' 、'c' 三种字母。
如果不存在这样的字符串 s ，请返回一个空字符串 ""。



示例 1：

输入：a = 1, b = 1, c = 7
输出："ccaccbcc"
解释："ccbccacc" 也是一种正确答案。
示例 2：

输入：a = 2, b = 2, c = 1
输出："aabbc"
示例 3：

输入：a = 7, b = 1, c = 0
输出："aabaa"
解释：这是该测试用例的唯一正确答案。


提示：

0 <= a, b, c <= 100
a + b + c > 0
"""
# 贪心算法：优先排列数量多的字符
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            cnt.sort(key=lambda x: -x[0])
            hasNext = False     # 判断是否还可以追加，防止死循环
            for i, (c, ch) in enumerate(cnt):
                if c <= 0:
                    break
                # 如果已经存在'aa'类似结尾
                if len(res) >= 2 and res[-2] == ch and res[-1] == ch:
                    continue
                hasNext = True
                res.append(ch)
                cnt[i][0] -= 1
                break
            if not hasNext:
                return ''.join(res)


if __name__ == "__main__":
    a, b, c = 1, 1, 7
    s = Solution()
    print(s.longestDiverseString(a, b, c))
