"""
剑指 Offer 30. 包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
调用 min、push 及 pop 的时间复杂度都是 O(1)。



示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.


提示：

各函数的调用总次数不超过 20000 次


注意：本题与主站 155 题相同：https://leetcode-cn.com/problems/min-stack/

通过次数205,267提交次数369,346
"""

"""
执行用时：52 ms, 在所有 Python3 提交中击败了87.24%的用户
内存消耗：18.9 MB, 在所有 Python3 提交中击败了5.24%的用户
"""
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.minStack = list()
        self.len = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.len == 0:
            self.minStack.append(x)
        else:
            self.minStack.append(min(x, self.minStack[-1]))
        self.len += 1

    def pop(self) -> None:
        if self.len != 0:
            self.minStack.pop()
            self.stack.pop()
            self.len -= 1

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()

if __name__ == "__main__":
    obj = MinStack()
    obj.push(3)
    obj.push(0)
    obj.push(1)
    obj.min()
