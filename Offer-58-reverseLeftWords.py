"""
剑指 Offer 58 - II. 左旋转字符串
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。



示例 1：

输入: s = "abcdefg", k = 2
输出: "cdefgab"
示例 2：

输入: s = "lrloseumgh", k = 6
输出: "umghlrlose"


限制：

1 <= k < s.length <= 10000
"""
"""
方法一测试：
新建两切片字符串，并将两切片拼接为结果字符串，无冗余操作，效率最高。

Python

# 运行时间: 0.01 秒
def func1(s):
    cut = len(s) // 3
    return s[:cut] + s[cut:]
方法二测试：
列表(Python) 和 StringBuilder(Java) 都是可变对象，每轮遍历拼接字符时，只是向列表尾部添加一个新的字符元素。
最终拼接转化为字符串时，系统 仅申请一次内存 。

Python

# 运行时间: 1.86 秒
def func2(s):
    res = []
    for i in range(len(s)):
        res.append(s[i])  # 仅需在列表尾部添加元素
    return ''.join(res)
方法三测试：
在 Python 和 Java 中，字符串是 “不可变对象” 。因此，每轮遍历拼接字符时，都需要新建一个字符串；因此，系统 需申请 NN 次内存 ，数据量较大时效率低下。

Python

# 运行时间: 6.31 秒
def func3(s):
    res = ""
    for i in range(len(s)):
        res += s[i]  # 每次拼接都需要新建一个字符串
    return res

"""
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


if __name__ == "__main__":
    string = "abcdefg"
    n = 2
    s = Solution()
    print(s.reverseLeftWords(string, n))
