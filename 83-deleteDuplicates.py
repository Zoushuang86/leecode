"""
83. 删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next

def myPrint(l: ListNode):
    r = []
    while l != None:
        r.append(l.val)
        l = l.next
    print(r)

"""
执行用时：52 ms, 在所有 Python3 提交中击败了57.54%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了6.58%的用户
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        else:
            l = head
            value = l.val
            while l.next != None:
                if l.next.val == value:
                    l.next = l.next.next
                else:
                    value = l.next.val
                    l = l.next
            return head

if __name__ == "__main__":
    l = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3, None)))))
    myPrint(Solution().deleteDuplicates(l))
