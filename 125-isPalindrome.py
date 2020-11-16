"""
125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false
"""

"""
执行用时：272 ms, 在所有 Python3 提交中击败了5.11%的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了23.60%的用户
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.isalnum()
        s = list(s.lower())
        print(s)

        slist = []
        for i in s:
            if i.isalnum():
                slist.append(i)
        print(slist)
        length = len(slist) // 2
        count = 0
        while count < length:
            count += 1

            if slist[0] == slist[-1]:
                slist.pop(0)
                slist.pop(-1)
            else:
                return False
            print(slist)
        return True

"""
执行用时：56 ms, 在所有 Python3 提交中击败了74.49%的用户
内存消耗：18.9 MB, 在所有 Python3 提交中击败了7.18%的用户
"""
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]

"""

"""
执行用时：56 ms, 在所有 Python3 提交中击败了74.49%的用户
内存消耗：18.6 MB, 在所有 Python3 提交中击败了20.69%的用户
"""
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(sgood)
        left, right = 0, n - 1
        
        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1
        return True
"""

if __name__ == "__main__":
    s = "race a car"
    print(Solution().isPalindrome(s))

