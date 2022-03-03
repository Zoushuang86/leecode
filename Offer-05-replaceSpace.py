"""
剑指 Offer 05. 替换空格
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。


示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."


限制：
0 <= s 的长度 <= 10000
"""
"""
可以字符串拼接，或者多申请两个空间存储
"""
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")


if __name__ == "__main__":
    string = "I am not happy."
    s = Solution()
    print(s.replaceSpace(string))
