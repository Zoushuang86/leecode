"""
344. 反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。



示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
"""

"""
执行用时：52 ms, 在所有 Python3 提交中击败了52.13%的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了10.54%的用户
"""
"""
class Solution:
    def reverseString(self, s):
        # Do not return anything, modify s in-place instead.
        s.reverse() # or s[:]=s[::-1]
"""
"""
执行用时：48 ms, 在所有 Python3 提交中击败了71.18%的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了9.66%的用户
"""
class Solution:
    def reverseString(self, s):
        left = 0
        right = len(s)-1
        while left < right:
            t = s[left]
            s[left] = s[right]
            s[right] = t
            left += 1
            right -= 1
        return s


if __name__ == "__main__":
    A = ["h","e","l","l","o"]
    s = Solution()
    print(s.reverseString(A))
