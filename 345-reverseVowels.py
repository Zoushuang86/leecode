"""
345. 反转字符串中的元音字母
给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。



示例 1：

输入：s = "hello"
输出："holle"
示例 2：

输入：s = "leetcode"
输出："leotcede"


提示：

1 <= s.length <= 3 * 105
s 由 可打印的 ASCII 字符组成
"""
"""
执行用时：64 ms, 在所有 Python3 提交中击败了24.36%的用户
内存消耗：15.7 MB, 在所有 Python3 提交中击败了43.23%的用户
"""
class Solution:
    def reverseVowels(self, s):
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        temp = list(s)
        left, right = 0, len(temp)-1
        while left < right:
            if temp[left] in vowels and temp[right] in vowels:
                temp[left], temp[right] = temp[right], temp[left]
                left += 1
                right -= 1
            elif temp[left] not in vowels:
                left += 1
            elif temp[right] not in vowels:
                right -= 1
        return "".join(temp)


if __name__ == "__main__":
    A = "leetcode"
    s = Solution()
    print(s.reverseVowels(A))
