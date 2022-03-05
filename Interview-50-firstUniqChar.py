"""
面试题50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:

输入：s = "abaccdeff"
输出：'b'
示例 2:

输入：s = ""
输出：' '


限制：

0 <= s 的长度 <= 50000
"""
from collections import defaultdict

class Solution:
    # 使用hash表存储最小索引，重复出现索引为-1
    def firstUniqChar(self, s: str) -> str:
        freq = defaultdict(int)
        for i, e in enumerate(s):
            if e in freq:
                freq[e] = -1
            else:
                freq[e] = i

        index = len(s)
        key = " "
        for k, v in freq.items():
            if v != -1 and v < index:
                index = v
                key = k
        return key


if __name__ == "__main__":
    A = "abavvdeds"
    s = Solution()
    print(s.firstUniqChar(A))
