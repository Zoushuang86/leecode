"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""

"""
执行用时：36 ms, 在所有 Python3 提交中击败了91.22%的用户
内存消耗：13.3 MB, 在所有 Python3 提交中击败了72.98%的用户
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        else:
            stack = []
            mapping = {")": "(", "}": "{", "]": "["}
            for i in range(len(s)):
                if len(stack) == 0:
                    stack.append(s[i])
                else:
                    if s[i] not in mapping.keys():
                        stack.append(s[i])
                    else:
                        if stack[-1] == mapping[s[i]]:
                            stack.pop(-1)
                        else:
                            return False
            if len(stack) != 0:
                return False
            else:
                return True


if __name__ == "__main__":
    x = ""
    s = Solution()
    print(s.isValid(x))
