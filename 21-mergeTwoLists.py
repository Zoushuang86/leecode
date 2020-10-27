"""
21. 合并两个有序链表
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。



示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""

"""
执行用时：52 ms, 在所有 Python3 提交中击败了47.02%的用户
内存消耗：13.6 MB, 在所有 Python3 提交中击败了5.41%的用户
"""
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l2 == None:
            return l1
        elif l1 == None:
            return l2
        else:
            l3 = None
            while (l1 != None and l2 != None):
                if l1.val <= l2.val:
                    if l3 == None:
                        l3 = ListNode(l1.val)
                        head = l3
                    else:
                        l3.next = ListNode(l1.val)
                        l3 = l3.next
                    l1 = l1.next
                else:
                    if l3 == None:
                        l3 = ListNode(l2.val)
                        head = l3
                    else:
                        l3.next = ListNode(l2.val)
                        l3 = l3.next
                    l2 = l2.next
                Print(head)
            if l1 != None:
                l3.next = l1
            if l2 != None:
                l3.next = l2
            return head

def Print(r=None):
    p = []
    while (r != None):
        p.append(r.val)
        r = r.next
    print(p)

if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(2, ListNode(3)))
    Print(l1)
    Print(l2)
    s = Solution()
    r = s.mergeTwoLists(l1, l2)
    Print(r)


