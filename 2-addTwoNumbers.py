"""
2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
执行用时：68 ms, 在所有 Python3 提交中击败了93.43%的用户
内存消耗：13.5 MB, 在所有 Python3 提交中击败了16.39%的用户
"""
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = False
        p = ListNode(-1, None)
        head = p
        while l1 and l2:
            temp = l1.val + l2.val + flag
            p.next = ListNode(temp % 10, None)
            if temp >= 10:
                flag = True
            else:
                flag = False
            l1 = l1.next
            l2 = l2.next
            p = p.next
        if l1:
            while l1:
                temp = l1.val + flag
                p.next = ListNode(temp % 10, None)
                if temp >= 10:
                    flag = True
                else:
                    flag = False
                l1 = l1.next
                p = p.next
        if l2:
            while l2:
                temp = l2.val + flag
                p.next = ListNode(temp % 10, None)
                if temp >= 10:
                    flag = True
                else:
                    flag = False
                l2 = l2.next
                p = p.next
        if flag:
            p.next = ListNode(1, None)
        return head.next
