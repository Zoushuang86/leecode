"""
剑指 Offer 09. 用两个栈实现队列
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。
(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用
通过次数355,058提交次数498,833
"""
"""
执行用时：392 ms, 在所有 Python3 提交中击败了29.80%的用户
内存消耗：19.2 MB, 在所有 Python3 提交中击败了6.50%的用户
"""
class CQueue:

    def __init__(self):
        self.stackA = list()
        self.stackB = list()
        self.len = 0

    def appendTail(self, value: int) -> None:
        self.stackA.append(value)
        self.len += 1

    def deleteHead(self) -> int:
        if self.len == 0:
            return -1

        self.stackB = self.stackA[::-1]
        self.stackA.clear()
        res = self.stackB.pop()
        self.stackA = self.stackB[::-1]
        self.len -= 1
        return res


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()


if __name__ == "__main__":
    ops = ["CQueue", "deleteHead", "appendTail", "appendTail", "deleteHead", "deleteHead"]
    res = [[]]
    q = CQueue()
    res.append(q.deleteHead())
    res.append(q.appendTail(5))
    res.append(q.appendTail(2))
    res.append(q.deleteHead())
    res.append(q.deleteHead())
    print(res)
