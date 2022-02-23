"""
917. 仅仅反转字母
给你一个字符串 s ，根据下述规则反转字符串：

所有非英文字母保留在原有位置。
所有英文字母（小写或大写）位置反转。
返回反转后的 s 。



示例 1：

输入：s = "ab-cd"
输出："dc-ba"
示例 2：

输入：s = "a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
示例 3：

输入：s = "Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"


提示

1 <= s.length <= 100
s 仅由 ASCII 值在范围 [33, 122] 的字符组成
s 不含 '\"' 或 '\\'
"""
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        string = list(s)
        i, j = 0, len(string) - 1
        while i < j:
            # if not string[i].isalpha():
            if not (65 <= ord(string[i]) <= 90 or 97 <= ord(string[i]) <= 122):
                i += 1
            # elif not string[j].isalpha():
            elif not (65 <= ord(string[j]) <= 90 or 97 <= ord(string[j]) <= 122):
                j -= 1
            else:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1
        return "".join(string)


if __name__ == "__main__":
    nums = "Test1ng-Leet=code-Q!"
    s = Solution()
    print(s.reverseOnlyLetters(nums))
